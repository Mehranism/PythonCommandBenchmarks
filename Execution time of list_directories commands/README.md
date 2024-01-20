# Project Name

Execution Time of List Directories Commands

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Conclusion](#conclusion)
- [Contributing](#contributing)
- [License](#license)

## Description

This project aims to analyze the execution time of common list directories commands in Python for retrieving a list of folders within a directory. The project focuses on five commands: `os.scandir()`, `os.walk()`, `glob.glob()`, `pathlib.iterdir()`, and `os.listdir()`.

The project involves creating approximately 2000 subfolders with random names to simulate a real-world scenario. Each command is executed ten times at each stage of increasing the number of subfolders to ensure accurate calculations. The resulting time is the average execution time of the commands. It's important to note that the actual execution time may vary depending on hardware and software configurations. However, the relative speed of the commands compared to each other remains consistent and measurable.

## Installation

To use any of the above commands, follow the instructions below:

- `os.scandir()`:

```python
fu = [f.path for f in os.scandir(directory) if f.is_dir()]
```

This command provides an object that allows access to distinct properties such as `name`, `path`, etc., of the subfolders. You can directly access the complete path of each folder without the need for additional commands like `os.path.join()`.

- `os.walk()`:

```python
fu = [x[0] for x in os.walk(directory)]
```

This command is commonly used for traversing all subfolders of a directory, even in a nested manner. However, compared to other commands, it usually has a longer execution time and returns the root directory as well.

- `glob.glob()`:

```python
fu = glob.glob(directory + "/*/")
```

This command returns a list of the complete paths of each folder. Similar to `os.scandir()`, it doesn't provide direct access to other properties like `name`, requiring additional commands for separation.

- `pathlib.iterdir()`:

```python
dirname = pathlib.Path(directory)
fu = [f for f in dirname.iterdir() if f.is_dir()]
```

This function only returns the subfolders at the first level and requires an additional `Path` command for execution.

- `os.listdir()`:

```python
fu = [os.path.join(directory, o) for o in os.listdir(directory) if os.path.isdir(os.path.join(directory, o))]
```

This command is the most commonly used command for this purpose. If you only need the names of the folders, no additional commands are required, and the output is a list of folder names. However, if you need the complete address of each directory, you need to use additional commands like `os.path.join()`.

## Usage

To use the project, follow these steps:

1. Clone the repository.
2. Set up the required dependencies and environment.
3. Run the project file to execute the commands and measure the execution time.

## Results

The results of the execution time for each of the above commands relative to the number of subfolders are plotted in the graph below.

![Graph Image][]

## Conclusion

As observed in the graph, all commands exhibit linear behavior with different slopes relative to the number of subfolders. The `os.scandir()` command has the smallest slope, indicating a consistent and efficient performance regardless of the number of subfolders. On the other hand, `os.walk()` has the longest execution time compared to other commands and returns the root directory, unlike others.Based on these findings, it can be concluded that `os.scandir()` is the fastest and most stable command among the analyzed options. However, the choice of command may also depend on hardware capabilities and software configurations.

## Contributing

Contributions to this project are welcome. You can contribute by following these steps:1. Fork the repository.2. Create a new branch.3. Make your enhancements or bug fixes.4. Submit a pull request.

## Contact

For any questions, suggestions, or feedback, please feel free to contact us at [nkh.mehran@gmail.com](mailto:nkh.mehran@gmail.com).
