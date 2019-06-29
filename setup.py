from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='pig-tdd',
    version='1.0.0',
    packages=['game', 'game.test'],
    package_dir={'game': 'game'},
    url='https://github.com/oswal-dheeraj/pig-tdd',
    license='',
    author='Dheeraj Oswal',
    author_email='oswal-dheeraj@users.noreply.github.com',
    description='Step by step test driven pig game. Based on tutorial at http://www.codekoala.com/pdfs/tdd.pdf',
    long_description=readme()
)
