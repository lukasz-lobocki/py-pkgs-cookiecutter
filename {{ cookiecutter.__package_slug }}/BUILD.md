# {{ cookiecutter.package_name }}

## Typical build workflow

```bash
git add --update
```

```bash
git commit -m "fix: change"
```

```bash
poetry run semantic-release version
```

```bash
git push
```

## Cookiecutter initiation

```bash
cookiecutter \
  ssh://git@github.com/lukasz-lobocki/py-pkgs-cookiecutter.git \
  package_name="{{ cookiecutter.package_name }}"
```

### was run with following variables

- package_name: **`{{ cookiecutter.package_name }}`**;
package_short_description: `{{ cookiecutter.package_short_description }}`

- package_version: `{{ cookiecutter.package_version }}`; python_version: `{{ cookiecutter.python_version }}`

- author_name: `{{ cookiecutter.author_name }}`;
open_source_license: `{{ cookiecutter.open_source_license }}`

- __package_slug: `{{ cookiecutter.__package_slug }}`; include_github_actions: `{{ cookiecutter.include_github_actions }}`

### on

`{% now 'local', '%Y-%m-%d %H:%M:%S %z' %}`
