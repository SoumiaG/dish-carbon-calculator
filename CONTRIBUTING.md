# Contributing to Dish Carbon Calculator

First off, thank you for considering contributing to the Dish Carbon Calculator! 🌱

## 🤝 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates.

**When submitting a bug report, include:**
- Clear, descriptive title
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Your environment (OS, Python version, browser)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:
- Clear description of the enhancement
- Why this would be useful
- Any implementation ideas you have

### Pull Requests

1. **Fork the repo** and create your branch from `main`
2. **Make your changes** following the code style
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Write meaningful commit messages**
6. **Submit the pull request**

## 🏗️ Development Setup

### Prerequisites
- Python 3.8+
- Git
- Virtual environment tool (venv, conda)

### Setup Steps

```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/dish-carbon-calculator.git
cd dish-carbon-calculator

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install dev dependencies
pip install pytest black flake8 isort

# 5. Run tests
python test_example.py

# 6. Run the app
streamlit run app.py
```

## 📝 Code Style

### Python Code
- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small
- Maximum line length: 127 characters

### Format Before Committing
```bash
# Format code
black .

# Sort imports
isort .

# Check linting
flake8 .
```

### Example Good Code

```python
def calculate_carbon_footprint(ingredients: list, portions: dict = None) -> tuple:
    """
    Calculate total carbon footprint for given ingredients.
    
    Args:
        ingredients: List of ingredient names
        portions: Optional dict of custom portions in kg
        
    Returns:
        tuple: (total_footprint, breakdown_list)
    """
    if portions is None:
        portions = {}
    
    total_footprint = 0
    breakdown = []
    
    # Clear, focused logic here
    
    return total_footprint, breakdown
```

## 🧪 Testing

### Run Existing Tests
```bash
python test_example.py
```

### Adding New Tests
- Add test cases to `test_example.py`
- Ensure all tests pass before submitting PR
- Add tests for new features

## 📚 Documentation

### When to Update Docs
- New features → Update README.md
- API changes → Update ARCHITECTURE.md
- New examples → Update EXAMPLES.md
- Deployment changes → Update DEPLOYMENT.md

### Documentation Style
- Use clear, simple language
- Include code examples
- Add screenshots for UI changes
- Keep formatting consistent

## 🌿 Contribution Ideas

### 🟢 Good First Issues

**Easy**:
- Add more ingredients to database
- Improve error messages
- Fix typos in documentation
- Add more test cases
- Create example images

**Medium**:
- Improve ingredient detection accuracy
- Add new suggestion algorithms
- Enhance UI/UX
- Add data visualization
- Implement caching improvements

**Advanced**:
- Integrate Recipe1M+ dataset
- Add user authentication
- Implement database backend
- Create REST API
- Build mobile version

### 🎯 High-Impact Contributions

1. **Better AI Model**
   - Fine-tune on food images
   - Improve ingredient detection
   - Add portion size estimation

2. **Data Enhancement**
   - More ingredients
   - Regional carbon data
   - Seasonal variations
   - Cooking method impacts

3. **User Features**
   - User accounts
   - History tracking
   - Progress visualization
   - Social features

4. **Performance**
   - Optimize model loading
   - Reduce memory usage
   - Faster processing
   - Better caching

## 🔍 Code Review Process

1. **Automated checks** run via GitHub Actions
2. **Manual review** by maintainers
3. **Feedback** incorporated
4. **Approval** and merge

### What Reviewers Look For
- Code quality and style
- Test coverage
- Documentation updates
- Performance impact
- Security considerations

## 📋 Commit Message Guidelines

### Format
```
type(scope): subject

body (optional)

footer (optional)
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting, missing semicolons, etc.
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples

**Good**:
```
feat(carbon): add water footprint calculation

- Calculate water usage per ingredient
- Add water data to database
- Update UI to show water impact

Closes #42
```

**Bad**:
```
updated stuff
```

## 🐛 Finding Issues to Work On

- Check [Issues](https://github.com/YOUR_USERNAME/dish-carbon-calculator/issues)
- Look for `good first issue` label
- Look for `help wanted` label
- Comment on issue before starting work

## 💬 Communication

- **Questions?** Open a Discussion
- **Bugs?** Open an Issue
- **Feature ideas?** Open an Issue with `enhancement` label
- **Need help?** Tag maintainers in Issue/PR

## ⚖️ Code of Conduct

### Our Pledge
We're committed to making participation in this project a harassment-free experience for everyone.

### Our Standards

**Positive behavior**:
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what's best for the community
- Showing empathy towards others

**Unacceptable behavior**:
- Trolling, insulting/derogatory comments
- Public or private harassment
- Publishing others' private information
- Other unethical or unprofessional conduct

## 🏆 Recognition

Contributors will be:
- Listed in README.md
- Mentioned in release notes
- Credited in relevant documentation

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## 🙏 Thank You!

Your contributions make a real difference in promoting sustainable food choices! 🌱

**Questions?** Feel free to reach out via:
- GitHub Issues
- GitHub Discussions
- LinkedIn: [@soumia-ghalim](https://www.linkedin.com/in/soumia-ghalim/)

---

**Happy Contributing! 🚀**
