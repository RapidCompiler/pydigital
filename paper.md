---
title: 'PyDigital: A python package intended for visualizing digital data line coding, generating parity bits and detecting errors in parity encoded binary data'
tags:
  - Python
  - Digital Data
  - Line Coding
  - Parity Generation
  - LRC
  - VRC
  - CRC
  - Checksum
  - Unipolar NRZ
  - Unipolar RZ
  - Polar NRZ
  - Polar NRZL
  - Polar NRZI
  - Polar RZ
  - Bipolar NRZ
  - Bipolar RZ
  - Pseudoternary
  - IEEE Manchester
  - G E Thomas Manchester
  - Differential Manchester
authors:
  - name: Sanjay Suresh
    orcid: 0000-0002-8519-7898
    equal-contrib: true
    affiliation: 1
  - name: Prathish K V
    equal-contrib: true
    affiliation: 1
affiliations:
 - name: Independent Researcher, India
   index: 1
date: 5 October 2022

---

# PyDigital

[![PyPI version](https://img.shields.io/pypi/v/pydigital?color=44cc11&style=for-the-badge)](https://badge.fury.io/py/pydigital)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pydigital?style=for-the-badge)](https://python.org)
[![PyPI - Status](https://img.shields.io/pypi/status/django?style=for-the-badge)](https://pypi.org/project/pydigital/)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)

This python package __PyDigital__ provides visual representations of digital data line coding 📈 as well as generation of parity bits 🔢 and error detection for binary data.

The package can be used to prototype and visualize digital data transmission using the various line coding plots and the parity encoding and decoding functionalities.

If you like the package, feel free to 🌟 the repo and contribute to it! Also find us on Twitter [@PyDigital](https://twitter.com/).

## Installation

Install using `pip` with the command

```sh
$ pip install pydigital
```

## Usage
### Line Coding

```python
from pydigital import LineCoding

lc = LineCoding()

# Plots differential manchester line coding for the binary string
lc.diffmanchester('10010110')
```

> ❗ All line coding methods accept parameters in the form of strings, and arrays/tuples of integers/strings.

Different line coding techniques are available, all of which are listed below. 

| Method | Return Type |
| :---   | :---        |
|`unipolar_nrz (binary_string_literal)` | Plots input binary data in Unipolar NRZ |
|`unipolar_rz (binary_string_literal)` | Plots input binary data in Unipolar RZ |
|`polar_nrz (binary_string_literal)` | Plots input binary data in Polar NRZ |
|`polar_nrzl (binary_string_literal)` | Plots input binary data in Polar NRZL |
|`polar_nrzi (binary_string_literal)` | Plots input binary data in Polar NRZI |
|`polar_rz (binary_string_literal)` | Plots input binary data in Polar RZ |
|`bipolar_nrz (binary_string_literal)` | Plots input binary data in Bipolar NRZ |
|`bipolar_rz (binary_string_literal)` | Plots input binary data in Bipolar RZ |
|`pseudoternary (binary_string_literal)` | Plots input binary data in Pseudoternary |
|`manchester_ieee (binary_string_literal)` | Plots input binary data in IEEE Manchester |
|`manchester_gethomas (binary_string_literal)` | Plots input binary data in G.E.Thomas Manchester |
|`diffmanchester (binary_string_literal)` | Plots input binary data in Differential Manchester |


### Parity Encoding and Decoding

```python
from pydigital import ParityEncDec

pr = ParityEncDec()

vrc = pr.encode_vrc(['10110', '10100'])
print("VRC :", vrc[0])
print("DATA TRANSMITTED :", vrc[1])
# VRC : 10
# DATA TRANSMITTED : 101101 101000
        
vrc = pr.decode_vrc('101101 101000', 5, 2, 2)
print(vrc)
# THE DATA TRANSMITTED IS CORRECT
```
> ❗ Binary data are passed as string literals. Spaces are optional.

Encoding and decoding methods for four different types of parity techniques are given below.

|Method | Return Type|
| :---  | :---|
|`encode_lrc ([binary_string_literals])`| Array [LRC Bits, LRC Encoded Data]|
|`encode_vrc ([binary_string_literals])`| Array [VRC Bits, VRC Encoded Data]|
|`encode_crc (binary_string_literal, crc_key_string_literal)`| Array [CRC Bits, CRC Encoded Data]|
|`encode_checksum ([binary_string_literals])`| Array [Checksum Bits, Checksum Encoded Data]|
|`decode_lrc (binary_string_literal, bits_per_data_string, number_of_data_strings, return_type)`| Boolean, Decoded Data, or Text |
|`decode_vrc (binary_string_literal, bits_per_data_string, number_of_data_strings, return_type)`| Boolean, Decoded Data, or Text |
|`decode_crc (binary_string_literal, crc_key_string_literal, return_type)`| Boolean, Decoded Data, or Text |
|`decode_checksum (binary_string_literal, bits_per_data_string, number_of_data_strings, return_type)`| Boolean, Decoded Data, or Text |

## Development

To contribute to the package, first clone the repository and `cd` into it.
```sh
$ git clone https://github.com/RapidCompiler/pydigital.git
$ cd pydigital
```

Make changes inside the `pydigital` folder located in the `src` directory. You can then test this functionality either by creating a test file and importing the methods into it or by installing the package on your computer.

Create a virtual environment and activate it before you install the package locally.

```sh
$ python -m virtualenv env
$ env\Scripts\activate
$ pip install .
```
Run the `pip install .` command in the main project directory.

This project does not have a `setup.py` file and hence cannot be installed in the editable mode.
## Issues

You can report bugs and suggest improvements on this repository's [issue tracker](https://github.com/rapidcompiler/pydigital/issues)

## License
Designed and published with ♥ by Prathish K V ([@prathishkv](https://github.com/prathishkv)) and Sanjay S ([@rapidcompiler](https://github.com/rapidcompiler)) under MIT License[]()
