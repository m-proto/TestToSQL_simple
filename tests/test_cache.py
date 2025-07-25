import pytest
import time
from infrastructure.cache import CacheManager

@pytest.fixture
def cache():
    """Fixture pour créer une instance propre du CacheManager pour chaque test"""
    return CacheManager()

def test_cache_set_and_get(cache):
    """Test l'écriture et la lecture basique du cache"""
    cache.set("test_key", "test_value")
    assert cache.get("test_key") == "test_value"

def test_cache_expiration(cache):
    """Test l'expiration du cache"""
    # Mettre en cache avec un TTL de 1 seconde
    cache.set("test_key", "test_value", ttl=1)
    assert cache.get("test_key") == "test_value"
    
    # Attendre que le cache expire
    time.sleep(1.1)
    assert cache.get("test_key") is None

def test_cache_key_generation(cache):
    """Test la génération de clés de cache"""
    key1 = cache._generate_key("test", "data1")
    key2 = cache._generate_key("test", "data1")
    key3 = cache._generate_key("test", "data2")
    
    # Même données = même clé
    assert key1 == key2
    # Données différentes = clés différentes
    assert key1 != key3

def test_sql_result_caching(cache):
    """Test le cache spécifique aux requêtes SQL"""
    query = "SELECT * FROM test"
    result = {"data": [1, 2, 3]}
    
    # Test la mise en cache
    assert cache.cache_sql_result(query, result) is True
    
    # Test la récupération
    cached = cache.get_cached_sql_result(query)
    assert cached == result
    
    # Test avec une requête différente
    assert cache.get_cached_sql_result("SELECT * FROM other") is None

def test_cache_nonexistent_key(cache):
    """Test la récupération d'une clé inexistante"""
    assert cache.get("nonexistent") is None

def test_cache_overwrite(cache):
    """Test l'écrasement d'une valeur en cache"""
    cache.set("test_key", "value1")
    cache.set("test_key", "value2")
    assert cache.get("test_key") == "value2" 