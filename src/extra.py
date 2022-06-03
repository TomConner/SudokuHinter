from lxml import etree

parser = etree.XMLParser(resolve_entities=True)  # Noncompliant
tree1 = etree.parse('ressources/xxe.xml', parser)
root1 = tree1.getroot()
