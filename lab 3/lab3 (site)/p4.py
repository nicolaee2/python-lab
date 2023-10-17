def build_xml_element(tag, content, **kwargs):
    element = "<" + tag
    for key, value in kwargs.items():
        element += " " + key + "=\"" + value + "\""
    element += ">" + content + "</" + tag + ">"
    return element


print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))