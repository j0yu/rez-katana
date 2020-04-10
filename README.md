# Katana

[![CI](../..//workflows/CI/badge.svg?branch=master)](../../actions?query=workflow%3ACI+branch%3Amaster)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


[rez] package to install [Katana].

Here are some beginners instructions on how to use this repository.

## Installation

1. Install [rez] via `python install.py` method
1. Clone/download this repository
1. Ensure at least the folder printed by
   this command `rez config local_packages_path`
1. Open terminal in (extracted) repository folder,
   run `rez build --install`

Katana should now be installed as a [rez] package named `katana`.

## Usage

To run [Katana]: `rez env katana -- katana`


## Extra Topics

### Skip downloading installer

If you already have the **raw** Katana tar/zip downloaded from the Foundry's
website, place it inside the (extracted) repository folder without renaming it.

Then `rez build --install` should skip re-downloading the Katana tar/zip.

### Licensing

If you already have a license server setup, e.g. at the port and address 
`1234@licenseserver`, you can run Katana like:

```bash
rez env katana -- foundry_LICENSE=1234@licenseserver katana
```

There are many ways to go about setting up licenses for rez packages e.g.

1. Modify this rez package build to include your own custom `katana`
   launcher script which sets up your licenses
1. Have a separate `licenses` rez package to handle licenses used by your 
   studio. 
   
   This can then be added as a [requirement] e.g. `requires = ["licenses"]`

Which method you go by will depend on your current situation.


## Maintenance

Whenever new official release come out, update the `__version__`
in `package.py` then re-run `rez build --install`.

If you decide to make another install, e.g. new `commands()` environment
setup, you can instead just update the `+local.` version number to indicate
new releases/versions of your own. See [PEP 540 local version segments].

Also, you can rename `+local.` to something more relevant to you 
e.g. `+mystudio.` or  `+mygithubname.`

----

Want more rez packages? Checkout [my GitHub repositories][j0yu-rez-packages]

[rez]: https://github.com/nerdvegas/rez
[requirement]: https://github.com/nerdvegas/rez/wiki/Package-Definition-Guide#requires
[j0yu-rez-packages]: https://github.com/j0yu?tab=repositories&q=topic%3Arez+topic%3Apackage
[Katana]: https://www.foundry.com/products/katana
[PEP 540 local version segments]: https://www.python.org/dev/peps/pep-0440/#local-version-segments
