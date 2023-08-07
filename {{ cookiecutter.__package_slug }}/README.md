# {{ cookiecutter.__package_slug }} ![Static](https://img.shields.io/badge/[[RND_DICEWARE_PL]]-[[RND_DICEWARE_PL]]-[[RND_CSS_COLOR]]?style=for-the-badge&labelColor=[[RND_CSS_COLOR]])

{{ cookiecutter.package_short_description }}

## Installation as a submodule

```bash
poetry add --editable \
  git+ssh://git@github.com/lukasz-lobocki/{{ cookiecutter.__package_slug }}
```

## License

`{{ cookiecutter.__package_slug }}` was created by {{ cookiecutter.author_name }}. {% if cookiecutter.open_source_license != 'None' -%}It is licensed under the terms of the {{ cookiecutter.open_source_license }} license.{% else %}{{ cookiecutter.author_name }} retains all rights to the source and it may not be reproduced, distributed, or used to create derivative works.{% endif %}

All components used retain their original licenses.

## Credits

`{{ cookiecutter.__package_slug }}` was created with [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) and [template](https://github.com/lukasz-lobocki/py-pkgs-cookiecutter).
