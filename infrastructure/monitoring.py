"""
Monitoring et métriques pour la production
"""

import os
import time
import json
import psutil
from datetime import datetime
from typing import Dict, Any

from infrastructure.logging import logger
from infrastructure.settings import settings


class MetricsCollector:
    """Collecteur de métriques pour le monitoring"""

    def __init__(self):
        self.start_time = time.time()
        self.request_count = 0
        self.error_count = 0
        self.total_response_time = 0.0
        self.sql_generation_count = 0
        self.cache_hits = 0
        self.cache_misses = 0

    def record_request(self, response_time: float, success: bool = True):
        """Enregistre une requête"""
        self.request_count += 1
        self.total_response_time += response_time

        if not success:
            self.error_count += 1

        logger.info(
            "Request recorded",
            response_time=response_time,
            success=success,
            total_requests=self.request_count,
        )

    def record_sql_generation(self):
        """Enregistre une génération SQL"""
        self.sql_generation_count += 1

    def record_cache_hit(self):
        """Enregistre un hit cache"""
        self.cache_hits += 1

    def record_cache_miss(self):
        """Enregistre un miss cache"""
        self.cache_misses += 1

    def get_metrics(self) -> Dict[str, Any]:
        """Retourne les métriques actuelles"""
        uptime = time.time() - self.start_time
        avg_response_time = (
            self.total_response_time / self.request_count
            if self.request_count > 0
            else 0
        )

        # Métriques système
        memory_usage = psutil.virtual_memory()
        cpu_usage = psutil.cpu_percent()

        # Métriques cache
        cache_hit_rate = (
            self.cache_hits / (self.cache_hits + self.cache_misses)
            if (self.cache_hits + self.cache_misses) > 0
            else 0
        )

        return {
            "uptime_seconds": uptime,
            "requests_total": self.request_count,
            "errors_total": self.error_count,
            "error_rate": (
                self.error_count / self.request_count if self.request_count > 0 else 0
            ),
            "avg_response_time": avg_response_time,
            "sql_generations_total": self.sql_generation_count,
            "cache_hits": self.cache_hits,
            "cache_misses": self.cache_misses,
            "cache_hit_rate": cache_hit_rate,
            "system": {
                "memory_usage_percent": memory_usage.percent,
                "memory_available_mb": memory_usage.available / (1024 * 1024),
                "cpu_usage_percent": cpu_usage,
            },
        }


# Instance globale
metrics = MetricsCollector()


def get_system_health() -> Dict[str, Any]:
    """Retourne l'état de santé du système"""
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "healthy": True,
        "checks": {
            "memory": {
                "status": "healthy" if memory.percent < 80 else "warning",
                "usage_percent": memory.percent,
                "available_mb": memory.available / (1024 * 1024),
            },
            "disk": {
                "status": "healthy" if disk.percent < 80 else "warning",
                "usage_percent": disk.percent,
                "free_gb": disk.free / (1024 * 1024 * 1024),
            },
            "cpu": {"status": "healthy", "usage_percent": psutil.cpu_percent()},
        },
    }


def export_metrics_to_file(
    question: str, directory: str = "metrics_logs", filename: str = "metrics_all.json"
) -> None:
    """Ajoute les métriques à un fichier JSON unique"""
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)

    # Charger les métriques existantes si le fichier existe
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            all_metrics = json.load(f)
    else:
        all_metrics = []

    # Ajouter les nouvelles métriques avec timestamp et question
    metric_entry = metrics.get_metrics()
    metric_entry["timestamp"] = datetime.now().isoformat()
    metric_entry["question"] = question

    all_metrics.append(metric_entry)

    # Sauvegarder
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(all_metrics, f, ensure_ascii=False, indent=2)
