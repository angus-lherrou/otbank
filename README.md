# OTbank
OTbank is a databank of constraints used in [Optimality Theory](https://en.wikipedia.org/wiki/Optimality_Theory), a contemporary, constraint-based model of phonological theory. OTbank's goal is to provide a unified collection of OT constraints and common definitions for those constraints.
## Implementation details
OTbank is built with [Django](https://www.djangoproject.com/) 2.2.7.
## Motivation
As Optimality Theory is a relatively young model and conceptions of constraints are nebulous and vary from author to author, there is motivation for a resource for:
* finding constraints that have been proposed and [used in the literature](http://roa.rutgers.edu/), and
* understanding how they are defined and used by different authors.

Also, from a theoretical standpoint, it is useful to have a unified list of constraints, since classical OT holds that the set of constraints is universal and instantiated completely in every language.
## Progress
OTbank is in the early stages of development. As of now, it currently can display a list of constraints and a list of definitions for each constraint, with tooltips for citations.
## Planned features
Currently, features to be implemented are as follows:
* Modern UI
* User submission for additional constraints and definitions
* LaTeX integration with [ot-tableau](https://ctan.org/pkg/ot-tableau) for dynamic tableau generation
* Expansion into other linguistics domains, such as OT Syntax
## Contact
For more information, contact me at lherrou@brandeis.edu.
