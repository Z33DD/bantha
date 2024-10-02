import json
from genson import SchemaBuilder
from datamodel_code_generator.__main__ import main
import typer


app = typer.Typer()


@app.command()
def generate_schema(
    source_path: str = typer.Argument(
        ...,
        help="Path to the source JSON file",
    ),
    schema_name: str = typer.Argument(
        ...,
        help="Name of the generated schema",
    ),
    destination_path: str = typer.Option(
        ".",
        help="Path to the destination directory",
    ),
):
    with open(source_path, "r") as fp:
        source = json.load(fp)

    builder = SchemaBuilder()
    if isinstance(source, list):
        for event in source:
            builder.add_object(event)
    else:
        builder.add_object(source)

    schema = builder.to_schema()

    schema_file = destination_path + f"/{schema_name}.schema.json"

    with open(schema_file, "w") as fp:
        json.dump(schema, fp, indent=2)
        print(f"JSON Schema file generated at {schema_file}")

    model_file = destination_path + f"/{schema_name}.py"

    main(
        [
            "--input",
            schema_file,
            "--output",
            model_file,
            "--class-name",
            schema_name,
        ]
    )


if __name__ == "__main__":
    app()
