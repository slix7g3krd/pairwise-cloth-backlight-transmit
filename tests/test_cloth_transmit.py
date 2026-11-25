import pytest
import graphics.cloth_transmit as mod

CASES = [
    ("thickness_transmit", (1,)),
    ("two_sided_normal", (1,)),
    ("multi_layer_transmit", (1,)),
    ("per_light_transmit", (1,)),
    ("lod_normal_rebuild", (1,)),
    ("temporal_stable", (1,)),
    ("load_cloth", (1,)),
    ("shade_cloth", (1,)),
    ("resolve_cloth", (1,)),
    ("present_cloth", (1,)),
    ("validate_cloth", (1,)),
    ("metrics_cloth", (1,)),
    ("audit_cloth", (1,)),
    ("fallback_cloth", (1,)),
    ("determinism_cloth", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
