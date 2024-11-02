from dagster import Definitions, load_assets_from_package_module

from pipeline.assets import basic_qa_rag
from pipeline.resources import RESOURCES

defs = Definitions(
    assets=[
        *load_assets_from_package_module(basic_qa_rag, "basic_qa_rag", "basic_qa_rag"),
    ],
    resources=RESOURCES,
)
