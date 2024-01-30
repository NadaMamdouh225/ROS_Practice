from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nadamamdouh',
    maintainer_email='nada20011002@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "draw_c = my_robot_controller.draw_circle:main",
            "robot_news_station = my_robot_controller.robot_news_station:main",
            "smartphone_node = my_robot_controller.smartphone:main",
            "number_publisher = my_robot_controller.number_station:main",
            "number_counter = my_robot_controller.number_counter:main"
        ],
    },
)
