import re
from os import walk, path

output = './SUMARIO.md'
md_text = '# Sumário\n\n'


def norm(text):
    return re.sub(' ', '_', text)


def filtering(options):
    root, _dirs, files = options
    names = [name for name in files if name.lower().endswith('.md')
             or name.lower() != 'SUMARIO.md']
    if not root.startswith('./.') and names:
        return True


def mapping_md(options):
    names = [name for name in options[-1] if name.lower().endswith('.md')
             and name.lower() != 'sumario.md']
    if names:
        new_options = [*options[0:2], names]
        return new_options
    else:
        return False


def get_topics(path):
    topicExpression = re.compile(r'\#+\s.+')
    content = ''
    with open(path, 'r') as f:
        content = f.read()
    topics = re.findall(topicExpression, content)
    assemlbingTopics = []
    for topic in topics:
        header = {}
        sharp, name = topic.split(' ', 1)
        header['indent'] = len(sharp)
        header['name'] = name
        assemlbingTopics.append(header)
    return assemlbingTopics


filtered = list(filter(filtering, walk('.')))
filtered = list(map(mapping_md, filtered))

md_files = []

for root, dirs, files in filtered[1:]:
    for name in files:
        indice = {'path': path.join(root, name)}
        chapter = root.split('/')[-1].split('_')
        indice['chapter_number'] = chapter[0]
        indice['chapter_name'] = chapter[1]
        md_files.append(indice)


for chapter in md_files:
    if chapter['chapter_name'] not in ['Fontes']:
        chapter['topics'] = get_topics(chapter['path'])
md_files.append({
    'chapter_name': 'Fontes',
    'chapter_number': '9999',
    'path': './FONTES.md',
    'topics': [{'idx': 1, 'name': 'Fontes'}]
})


def create_sumary(items):
    summary = '\n'.join([create_entry(item) for item in items])
    return summary


def create_entry(item):
    chap_number = int(item['chapter_number'])
    title = f"{chap_number}. "
    if item['topics'][0]['name'] in ['Fontes']:
        title += f"[{item['topics'][0]['name']}]({item['path']})  "

    else:
        title += f"[Capítulo {item['chapter_number']} - {item['topics'][0]['name']}]({item['path']})  "
        
    lines = [title]
    for sec_title in item['topics'][1:]:
        name = sec_title['name']
        indent = sec_title['indent']
        sec_text = f"{'  '*indent} {chap_number}.1 [{name}]"
        sec_text += f"({item['path']}#{norm(name)})  "
        lines.append(sec_text)
    return '\n'.join(lines) + '\n'


def write_sumary(path, content):
    with open(path, 'w') as f:
        f.write(content)


md_text += create_sumary(md_files)
md_text += f"\n\n<<< voltar [Introdução](./README.md)  \n\>\>\> avançar [{md_files[0]['chapter_name']}]({md_files[0]['path']})"
write_sumary(output, md_text)
