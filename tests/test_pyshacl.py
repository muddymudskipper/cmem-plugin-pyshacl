"""Plugin tests."""
from cmem_plugin_pyshacl.plugin_pyshacl import ShaclValidation
from cmem.cmempy.dp.proxy.graph import post, get, delete
from uuid import uuid4

def test_execution():
    """Test plugin execution"""
    shacl_graph_uri = f"https://example.org/pyshacl-plugin-test/{uuid4()}"
    data_graph_uri = shacl_graph_uri
    validation_graph_uri = f"https://example.org/pyshacl-plugin-test/{uuid4()}"
    generate_graph = "1"
    output_values = "1"
    owl_imports_resolution = "1"
    post(shacl_graph_uri, "tests/shacl-shacl.nt", replace=True)
    response = get(shacl_graph_uri)
    if response.status_code != 200:
        raise ValueError(f"Response {response.status_code}: {response.url}")
    plugin = ShaclValidation(
        data_graph_uri=data_graph_uri,
        shacl_graph_uri=shacl_graph_uri,
        validation_graph_uri=validation_graph_uri,
        generate_graph=generate_graph,
        output_values=output_values,
        owl_imports_resolution=owl_imports_resolution)
    result = plugin.execute()
    response = get(validation_graph_uri)
    if response.status_code != 200:
        raise ValueError(f"Response {response.status_code}: {response.url}")
    delete(shacl_graph_uri)
    delete(validation_graph_uri)


