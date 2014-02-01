# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class SVG(object):
    def __init__(self):
        self.width = 100
        self.height = 100
        self.svg_string = ''

    @property
    def svg_header(self):
        return '<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">'.format(**{
            'width': self.width, 'height': self.height
        })

    @property
    def svg_closer(self):
        return '</svg>'

    def to_string(self):
        return ''.join([self.svg_header, self.svg_string, self.svg_closer])

    def rect(self, x, y, width, height, **kwargs):
        self.svg_string += '<rect x="{x}" y="{y}" width="{width}" height="{height}" {kwargs}/>'.format(**{
            'x': x, 'y': y, 'width': width, 'height': height, 'kwargs': self.write_args(**kwargs)
        })

    def circle(self, cx, cy, r, **kwargs):
        self.svg_string += '<circle cx="{cx}" cy="{cy}" r="{r}" {kwargs}/>'.format(**{
            'cx': cx, 'cy': cy, 'r': r, 'kwargs': self.write_args(**kwargs)
        })

    def path(self, str, **kwargs):
        self.svg_string += '<path d="{str}" {kwargs}/>'.format(**{
            'str': str, 'kwargs': self.write_args(**kwargs)
        })

    def polyline(self, str, **kwargs):
        self.svg_string += '<polyline points="{str}" {kwargs}/>'.format(**{
            'str': str, 'kwargs': self.write_args(**kwargs)
        })

    def group(self, elements, **kwargs):
        self.svg_string += '<g {}>'.format(self.write_args(**kwargs))
        for element in elements:
            exec(element)
        self.svg_string += '</g>'

    def write_args(self, **kwargs):
        str = ''
        for key, value in kwargs.iteritems():
            if isinstance(value, dict):
                str += '{}="'.format(key)
                for key, value in value.iteritems():
                    str += '{}:{};'.format(key, value)
                str += '" '
            else:
                str += '{}="{}" '.format(key, value)
        return str