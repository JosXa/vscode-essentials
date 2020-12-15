"""
Strips comments from the configuration.json file and writes the result into package.json
"""
import json
import re
from pathlib import Path

pkgjson_file = (Path(__file__).parent / "package.json")

package_json = json.loads(pkgjson_file.read_text())


config_json_content = (Path(__file__).parent / "extension-configuration.json").read_text()
sanitized = re.sub(r'\/\/.*$', '', config_json_content, flags=re.MULTILINE)
config_json = json.loads(sanitized)

package_json["extensionPack"] = config_json["extensionPack"]
pkgjson_file.write_text(json.dumps(package_json, indent=4))



