"""Dependency-free static publication checks; run from the repository root."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json
import struct
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://raemerrr.github.io'
APP = '/3d-lotto-number-generator/'
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(); self.tags=[]; self.ids=set(); self.refs=[]; self.ld=False
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); self.tags.append((tag,a))
        if 'id' in a: self.ids.add(a['id'])
        for key in ('href','src'):
            if key in a: self.refs.append(a[key])
        if tag=='script':
            assert a.get('type')=='application/ld+json', 'Unexpected executable script'
            self.ld=True
    def handle_data(self, data):
        if self.ld and data.strip(): json.loads(data)
    def handle_endtag(self, tag):
        if tag=='script': self.ld=False
pages={p:Page(ROOT/p) for p in ('index.html','privacy.html','404.html')}
for name, page in pages.items():
    assert ('html',{'lang':'ko'}) in page.tags
    assert sum(t=='h1' for t,a in page.tags)==1
    assert any(t=='title' for t,a in page.tags)
    if name!='404.html':
        expected=BASE+('/' if name=='index.html' else '/'+name)
        assert any(t=='link' and a.get('rel')=='canonical' and a.get('href')==expected for t,a in page.tags)
        assert any(t=='meta' and a.get('name')=='description' and a.get('content') for t,a in page.tags)
    for ref in page.refs:
        u=urlsplit(ref)
        if u.scheme or ref==APP: continue
        target=u.path.lstrip('/') or name
        if ref.startswith('#'): target=name
        if target=='index.html' or u.path=='/': target='index.html'
        assert (ROOT/target).is_file(), (name,ref)
        if u.fragment: assert u.fragment in pages[target].ids, (name,ref)
locs=[e.text for e in ET.parse(ROOT/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert set(locs)=={BASE+'/',BASE+'/privacy.html'}
robots=(ROOT/'robots.txt').read_text()
assert 'Disallow:' not in robots
assert BASE+'/sitemap.xml' in robots and BASE+APP+'sitemap.xml' in robots
assert not (ROOT/'ads.txt').exists()
assert struct.unpack('!II',(ROOT/'assets/og.png').read_bytes()[16:24])==(1200,630)
# WCAG relative luminance ratios for body text, secondary text and CTA.
def luminance(h):
    c=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    return sum(v*w for v,w in zip([v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in c],(.2126,.7152,.0722)))
for fg,bg in [('172b27','f6f5ef'),('4d6059','f6f5ef'),('4d6059','e9ece3'),('ffffff','165c43'),('165c43','f6f5ef')]:
    a,b=sorted((luminance(fg),luminance(bg)))
    ratio=(b+.05)/(a+.05); assert ratio>=4.5
    print(f'Contrast #{fg}/#{bg}: {ratio:.2f}:1')
print('PASS: Korean metadata, internal links/anchors, structured data, sitemap, robots, OG dimensions, no ads.txt or executable scripts')
