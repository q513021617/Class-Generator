# Class Generator
A command line tool used to take away all the fun of writing object classes

## Using the tool
### In the command line
For help:
'''
python ClassGenerator.py [-h]
'''

For java:
'''
python ClassGenerator.py [-g] [-s] [-t] [-k] [-c classname] [-e extends] [-i implements] Type Variable ...
'''

### Definitions
Options:
    -h or --help            Shows how to use the tool
    -c or --classname       Name of the class
    -e or --extends         Name of what is being extended
    -i or --implements      Name of what is being implemented
    -g or --getters         Generates getters
    -s or --setters         Generates setters
    -t or --toString        Creates a toString method
    -k or --clone           Creates a clone method

Arguments:
    Type            The type of the variable
    Variable        The name of the variable

## Example
### Console input
```
python ClassGenerator.py -g -s -t -k -c doe -e deer -i animal double a float f string str
```

### Console output
```
Valid input
Generating doe.java file
File, ./Output/doe.java, has been created
End of execution
```

### File output
```
public class doe extends deer implements animal
{

	private double a;
	private float f;
	private string str;

	public doe()
	{

	}

	public doe(double a, float f, string str)
	{
		this.a = a;
		this.f = f;
		this.str = str;
	}

	public void setA(double a)
	{
		this.a = a;
	}

	public void setF(float f)
	{
		this.f = f;
	}

	public void setStr(string str)
	{
		this.str = str;
	}

	public double getA()
	{
		return a;
	}

	public float getF()
	{
		return f;
	}

	public string getStr()
	{
		return str;
	}

	public string toString()
	{
		return "doe: a = " + a + ", f = " + f + ", str = " + str;
	}

	public doe clone()
	{
		doe newDoe = new doe(a, f, str)
		return newDoe;
	}

}
```

## Dependencies
python 2 to run the program

# Future work
Add more languages
