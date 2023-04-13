<p align="center">
  <img src="docs/img.jpeg" width="50%" height="50%">
</p>

# ✨ Table of contents
- [✨ Table of contents](#-table-of-contents)
- [🎉 Set up the environment](#-set-up-the-environment)
- [📚 Install new packages](#-install-new-packages)
- [💾 Contribute](#-contribute)
- [💥 Linting](#-linting)


# 🎉 Set up the environment
1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Set up the environment:
```bash
make activate
make setup
```

# 📚 Install new packages
To install new PyPI packages, run:
```bash
poetry add <package-name>
```


# 💾 Contribute
Add and push all changes to Git:
```bash
git add .
git commit -m 'commit-message'
git push origin <branch>
```

# 💥 Linting
```shell
poetry run pylint openresa-bot
```





