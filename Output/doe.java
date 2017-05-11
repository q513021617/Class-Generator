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
