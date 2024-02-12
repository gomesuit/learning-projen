from projen.python import PythonProject

project = PythonProject(
    author_email="9404411+gomesuit@users.noreply.github.com",
    author_name="gomesuit",
    module_name="learning_projen",
    name="learning-projen",
    version="0.1.0",
)

project.synth()