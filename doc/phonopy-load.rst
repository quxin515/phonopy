.. _phonopy_load_command:

phonopy-load command
====================

At phonopy v2.7.0, ``phonopy-load`` command is installed. This behaves
similarly to ``phonopy.load`` (:ref:`phonopy_load`) in the phonopy
python module. The main aim of introducing this command is to provide
uniform usage over many different force calculators. Once
``phonopy_disp.yaml`` is created, the later operations will be the
same using this command.

The following default behaviours are changed from that of those
of ``phonopy`` command:

1. ``phonopy_xxx.yaml`` type file is always necessary by a way of (2)
   or (3).
2. The first argument of the command is used to give a ``phonopy_xxx.yaml``
   type file.
3. The file names of ``phonopy_params.yaml``, ``phonopy_disp.yaml``,
   ``phonopy.yaml`` are the default file
   names and these files are searched in the current directory. The
   preference order is as given here.
4. ``-c`` option (read crystal structure) does not exist.
5. Use of dommand options is recommended, but phonopy configuration
   file can be read using ``--config`` option.
6. If parameters for non-analytical term correction (NAC) are
   found, NAC is automatically enabled. This can be disabled by
   ``--nonac`` option.
7. When force constants are calculated from displacements and forces
   dataset, force constants are automatically symmetrized. To disable
   this, ``--no-sym-fc`` option is used.

Examples
--------

In the NaCl-qe example,

::

   % phonopy --qe -d --dim 2 2 2 --pa auto -c NaCl.in
   % phonopy -f NaCl-00{1,2}.out

With these commands, ``phonopy_disp.yaml`` and ``FORCE_SETS`` are
created. After this step, it is unnecessary to specify ``--qe`` option
to run with ``phonopy-load``. The following command works to draw band
structure.

::

   % phonopy-load --band auto -p

Data in ``FORCE_SETS`` and ``BORN`` stored in
``phonopy_xxx.yaml`` file can be used as follows::

   % phonopy-load --include-all
   % mkdir test && cd test
   % mv ../phonopy.yaml phonopy_data.yaml
   % phonopy-load phonopy_data.yaml --band auto -p
