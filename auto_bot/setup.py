from setuptools import find_packages, setup
import os
package_name = 'auto_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), ['launch/compete_launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='masa',
    maintainer_email='masamostafa2017@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
          'compete = auto_bot.compete:main',
          'manual=auto_bot.manual:main',
          'camera_node=auto_bot.camera_node:main',
          'view_detection=auto_bot.view_detection:main'
        ],
    },
)
