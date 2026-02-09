from brain_core import CIPipelineValidator

validator = CIPipelineValidator()

# change this path to any real JSON config file you have
result = validator.validate_file_dict("notebooks/sample.json")


print(result)
