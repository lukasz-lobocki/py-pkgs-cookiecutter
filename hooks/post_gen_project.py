import os
import shutil
import random
import re
import requests

##############################################################################
# Utilities
##############################################################################


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


def replace_placeholder(file_path, placeholder, replacer):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        while re.search(placeholder, content):
              color = replacer()
              content = re.sub(placeholder, color, content, count=1)

        with open(file_path, 'w') as file:
            file.write(content)

        print(f"\nPlaceholders {placeholder} in {file_path} replaced.")
    
    except FileNotFoundError:
        print(f"\nFile {file_path} not found.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

def pick_random_css_color():
    css_colors = [
        'black', 'silver', 'gray', 'white', 'maroon', 'red', 'purple', 'fuchsia',
        'green', 'lime', 'olive', 'yellow', 'navy', 'blue', 'teal', 'aqua',
        'orange', 'aliceblue', 'antiquewhite', 'aquamarine', 'azure', 'beige',
        'bisque', 'blanchedalmond', 'blueviolet', 'brown', 'burlywood', 'cadetblue',
        'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson',
        'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen',
        'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid',
        'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray',
        'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray',
        'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'gainsboro',
        'ghostwhite', 'gold', 'goldenrod', 'greenyellow', 'honeydew', 'hotpink',
        'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush',
        'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan',
        'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightpink',
        'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray',
        'lightsteelblue', 'lightyellow', 'limegreen', 'linen', 'magenta',
        'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple',
        'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise',
        'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin',
        'navajowhite', 'oldlace', 'olivedrab', 'orangered', 'orchid', 'palegoldenrod',
        'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff',
        'peru', 'pink', 'plum', 'powderblue', 'rosybrown', 'royalblue', 'saddlebrown',
        'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'skyblue',
        'slateblue', 'slategray', 'snow', 'springgreen', 'steelblue', 'tan',
        'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'whitesmoke',
        'yellowgreen'
    ]
    return random.choice(css_colors)

def pick_random_diceware_pl():
    response = requests.get("https://github.com/MaciekTalaska/diceware-pl/raw/master/diceware-pl.txt")
    if response.status_code == 200:
        lines = response.text.split('\n')
        lines = [line.strip() for line in lines if line.strip()]
    else:
        print(f"Failed to load content from {url}. Status code: {response.status_code}")
        return
        # Return a random line
    return random.choice(lines)

##############################################################################
# Cookiecutter clean-up
##############################################################################

if "{{cookiecutter.include_github_actions}}" == "no":
    remove(".github/")
else:
    for root, dirs, files in os.walk(".github/workflows/"):
        for name in files:
            if not name.endswith("%s.yml" % "{{cookiecutter.include_github_actions}}"):
                remove(os.path.join(root, name))

# Remove license (if specified)
if "{{cookiecutter.open_source_license}}" == "None":
    remove("LICENSE")

##############################################################################
# README.md placeholders randomization
##############################################################################

replace_placeholder("README.md", r'\[\[RND_CSS_COLOR\]\]', pick_random_css_color)
replace_placeholder("README.md", r'\[\[RND_DICEWARE_PL\]\]', pick_random_diceware_pl)
