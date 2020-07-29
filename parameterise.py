import os
import xml.etree.ElementTree as ET

# Add qgis symbol parameters to SVG files

# Built on the work of raymondnijssen https://github.com/IFRCGo/IFRC-Icons/blob/master/OCHA_Icons_2018/scripts/convert_to_qgis.py

root_dir = os.path.dirname(os.path.realpath(__file__))
svg_dir = os.path.join(root_dir, 'collections/font_awesome/svg')

svgNs = 'http://www.w3.org/2000/svg'
ET.register_namespace('', svgNs)

tags = ('path', 'polygon', 'circle', 'rect')
uriPrefixedTags = ['{{{0}}}'.format(svgNs) + s for s in tags]

qgisStylingAttributes = {'fill': 'param(fill)',
                     'stroke': 'param(outline)',
                     'stroke-width': 'param(outline-width) 0',
                     'fill-opacity': 'param(fill-opacity)',
                     'stroke-opacity': 'param(outline-opacity)'}

for dirpath, dirs, files in os.walk(svg_dir):
    for f in files:
        filename = os.path.join(dirpath, f)
        try:
            if filename.endswith(".svg"): 
                tree = ET.parse(filename)
                root = tree.getroot()
                for element in root.iter():
                    if element.tag in uriPrefixedTags:
                        element.attrib.pop('class', None)
                        element.attrib.update(qgisStylingAttributes)

                tree.write(filename, encoding='utf-8')
                print(filename)

        except Exception as err:
            print(err)

