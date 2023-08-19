Traceback(most recent call last):
  File "/Users/mcl/Platformer/venv/bin/autopep8", line 8, in <module >
    sys.exit(main())
             ^ ^ ^ ^ ^^
  File "/Users/mcl/Platformer/venv/lib/python3.11/site-packages/autopep8.py", line 4512, in main
    fixed_stdin = fix_code(read_stdin, args, encoding=encoding)
                  ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
  File "/Users/mcl/Platformer/venv/lib/python3.11/site-packages/autopep8.py", line 3506, in fix_code
    return fix_lines(sio.readlines(), options=options)
           ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
  File "/Users/mcl/Platformer/venv/lib/python3.11/site-packages/autopep8.py", line 3569, in fix_lines
    fixed_source = fix.fix()
                   ^ ^ ^ ^ ^ ^ ^ ^ ^
  File "/Users/mcl/Platformer/venv/lib/python3.11/site-packages/autopep8.py", line 613, in fix
    self._fix_source(filter_results(source=''.join(self.source),
  File "/Users/mcl/Platformer/venv/lib/python3.11/site-packages/autopep8.py", line 557, in _fix_source
    modified_lines=fix(result)
                     ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
  File "/Users/mcl/Platformer/venv/lib/python3.11/site-packages/autopep8.py", line 761, in fix_e225
    pycodestyle.missing_whitespace_around_operator(fixed, ts))
    ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
AttributeError: module 'pycodestyle' has no attribute 'missing_whitespace_around_operator'. Did you mean: 'whitespace_around_operator'?
