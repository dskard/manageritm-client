# CHANGELOG



## v0.1.0 (2023-10-28)

### Ci

* ci: use pyenv virtualenv-delete instead of pyenv uninstall

Updating Makefile to use pyenv virtualenv-delete to delete the virtual
environment instead of pyenv uninstall. Also, I think the hooks are
properly being created in pyenv now, so we don&#39;t need to install black,
pytest, and pdbpp outside of poetry. We can run poetry install to get
all of the pieces installed. ([`cbb8c26`](https://github.com/dskard/manageritm-client/commit/cbb8c26de26fe0f42f8d1679c3549005c4ef98b2))

* ci: reworking release action ([`72b9044`](https://github.com/dskard/manageritm-client/commit/72b9044035e5fec9f182da48bf1a9879b18e6d37))

### Feature

* feat: support sending additional_flags and command to endpoints

When using the /client/proxy endpoint, users can send additional command
line options to the proxy command. In the call to `...client()`, set the
`additional_flags` parameter to a list of flags to be appended to the
default command.

Example:
```
client.client(
    additional_flags=[&#34;--opt1&#34;, &#34;value1&#34;, &#34;--opt2&#34;, &#34;value2&#34;]
)
```

When using the /client/command endpoint, users can set the command to
run. In the call to `...client()`, set the `command` parameter to a list
of version of the command to run.

Example:
```
client.client(command=[&#34;sleep&#34;, &#34;200000000000&#34;])
```

Added test cases for the new features. ([`ab5cd60`](https://github.com/dskard/manageritm-client/commit/ab5cd60644df5aa02bbec5d6d76ac856182dd649))

### Unknown

* Merge pull request #1 from dskard/dsk-initial-upload

feat: initial upload ([`8e33dfe`](https://github.com/dskard/manageritm-client/commit/8e33dfe45a63e61ce9fd0f0cb41d7594f1bf4229))

* initial upload ([`7157cfc`](https://github.com/dskard/manageritm-client/commit/7157cfce5c7e2315dc78997d9e32fad3f3e76c85))

* Initial commit ([`a0b0d9b`](https://github.com/dskard/manageritm-client/commit/a0b0d9b8b22fd8beb6d62105182c320da28780d8))
