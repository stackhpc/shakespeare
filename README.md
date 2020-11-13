# Rally tempest config generator

Generates tempest configuration overrides for rally

## Installation

### for python 3:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### for python 2:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage


### Download the recipes for your deployment

```
git clone https://github.com/stackhpc/tempest-recipes.git recipes
```

### Generate config files

```
ansible-playbook template.yml -e@recipes/candidate/baremetal-fix-ip.yml
```

where `candidate/baremetal-fix-ip.yml` is a path in the recipes repository.
