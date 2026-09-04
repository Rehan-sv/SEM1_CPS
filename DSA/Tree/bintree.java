package Tree;
class node
{
	node parent;
	node leftchild;
	node rightchild;
	int data;
	node(node parent,int data,node leftchild,node rightchild)
	{
		this.data=data;
		this.parent=parent;
		this.leftchild=leftchild;
		this.rightchild=rightchild;
	}
	public void setleft(node leftchild)
	{
		this.leftchild=leftchild;
	}
	public void setright(node rightchild)
	{
		this.rightchild=rightchild;
	}
	public void setdata(int data)
	{
		this.data=data;
	}
	public node getleft()
	{
		return leftchild;
	}
	public node getright()
	{
		return rightchild;
	}
	public int getdata()
	{
		return data;
	}
	public node getparent() {
		return parent;
	}
}
public class bintree {
	node root;
	int size;
	bintree()
	{
		root=null;
		size=0;
	}
	public void setroot(node n)
	{
		root=n;
	}
	public node getroot()
	{
		return root;
	}
	public node root()
	{
		return root;
	}
	public void insert(int data)
	{
		//empty tree
		if(root==null)
		{
			root=new node(null,data,null,null);
		}
		else
		{
			
			node prev=null;
			node temp=root;
			while(temp!=null)
			{
				prev=temp;
				if(temp.getdata()>data)
				{
					temp=temp.getleft();
				}
				else
				{
					temp=temp.getright();
				}
			}
			if(prev.getdata()>data)
			{
				prev.setleft(new node(prev,data,null,null));
			}
			else
			{
				prev.setright(new node(prev,data,null,null));
			}
        }
	}
	public void deletion(int key)
	{
		//empty tree
		if(root==null)
		{
			System.out.println("key not found");
			return;
		}
		//search for key location in binary search tree
		node prev=null;
		node temp=root;
		while(temp!=null && temp.getdata()!=key)
		{
			prev=temp;
			if(temp.getdata()>key)
			{
				temp=temp.getleft();
			}
			else
			{
				temp=temp.getright();
			}
		}
		//if key is not there
		if(temp==null)
		{
			System.out.println("key not found");
		}
		else
		{
			//checking for two children
			if(temp.getleft()!=null && temp.getright()!=null)
			{
				node succ = temp.getright();
				node sprev = temp;
				while(succ.getleft()!=null)
				{
					sprev=succ;
					succ=succ.getleft();
				}
				temp.setdata(succ.getdata());
				temp=succ;
				prev=sprev;
			}
			node child;
			if(temp.getleft()!=null)
			{
				child=temp.getleft();
			}
			else
			{
				child=temp.getright();
			}
			if(prev==null)
			{
				root=child;
			}
			else if(prev.getleft()==temp)
			{
				prev.setleft(child);
				if(child!=null)
				{
					child.parent=prev;
				}
			}
			else
			{
				prev.setright(child);
				if(child!=null)
				{
					child.parent=prev;
				}
			}
		}
		
	}
	 public void inorder(node temp) {
		                                                
	        if (temp == null) {
	            return;
	        }
            
	        inorder(temp.getleft());
	        System.out.print(temp.getdata() + " ");
	        inorder(temp.getright());
	    }
    public static void main(String [] args)
    {
    	bintree t = new bintree();
    	t.insert(90);
    	t.insert(80);
    	t.insert(70);
    	t.insert(60);
    	//t.deletion(90);
    	t.inorder(t.getroot());
    }
}