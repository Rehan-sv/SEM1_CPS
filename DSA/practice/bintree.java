package practice;

class Node {
    private Node parent;
    private String data;
    private Node leftChild;
    private Node rightChild;

    Node(Node parent, String data, Node leftChild, Node rightChild) {
        this.parent = parent;
        this.data = data;
        this.leftChild = leftChild;
        this.rightChild = rightChild;
    }

    public void setData(String data) {
        this.data = data;
    }

    public String getData() {
        return data;
    }

    public void setLeft(Node leftChild) {
        this.leftChild = leftChild;
    }

    public void setRight(Node rightChild) {
        this.rightChild = rightChild;
    }

    public Node getLeft() {
        return leftChild;
    }

    public Node getRight() {
        return rightChild;
    }

    public Node getParent() {
        return this.parent;
    }
    
}

public class bintree {
    private Node root;
    private int size;

    bintree() {
        root = null;
        size = 0;
    }

    public int getSize() {
        return size;
    }

    public void setRoot(Node n) {
        root = n;
    }

    public Node getRoot() {
        return root;
    }
    public int depth(Node v) {
    	if(v == null) 
    	{
    		return -1 ;
    	}
    	else {
    		return 1 + depth(v.getParent()) ; 
    	}
    }
    
    public int depth(Node v, String x) {
        if (v == null) {
            return -1;
        }
        else {
	        int dist = -1 ;
	        if (v.getData().equals(x) || (dist = depth(v.getLeft(), x)) >= 0 || (dist = depth(v.getRight(), x)) >= 0) {
	            return dist + 1;
	        }
	        return dist ;
        }
    }
    
    public int height(Node node) {
        if (node == null) {
            return -1;
        }
        int leftHeight = height(node.getLeft());
        int rightHeight = height(node.getRight());
        return 1 + ( (leftHeight > rightHeight ) ? leftHeight : rightHeight );
    }
    
    public void preorder(Node v) // ROOT --> LEFT --> RIGHT .
    {
    	if (v == null) return ;
    	else {
    		System.out.println(v.getData()) ;
    		preorder(v.getLeft()) ;
    		preorder(v.getRight() ) ; 
    	}
    }
    
    public void inorder(Node v) 
    {
    	if(v == null) return ; 
    	else {
    		inorder(v.getLeft()) ;
    		System.out.println(v.getData());
    		inorder(v.getRight()) ; 
    	}
    }
    
    public void postorder(Node v)
    {
        if (v == null) return;
        else {
	        postorder(v.getLeft());
	        postorder(v.getRight());
	        System.out.println(v.getData());
        }
    }
    
    public void insertNode(int data) 
    {
    	
    }
    
    public static void main(String[] args) {
        bintree t = new bintree();

        t.setRoot(new Node(null, "A", null, null));
        
        t.getRoot().setLeft(new Node(t.getRoot(), "B", null, null));
        t.getRoot().setRight(new Node(t.getRoot(), "C", null, null));

        t.getRoot().getLeft().setLeft(new Node(t.getRoot().getLeft(), "D", null, null));
        t.getRoot().getLeft().setRight(new Node(t.getRoot().getLeft(), "E", null, null));

        t.getRoot().getRight().setLeft(new Node(t.getRoot().getRight(), "F", null, null));
        t.getRoot().getRight().setRight(new Node(t.getRoot().getRight(), "G", null, null));

        System.out.println("Root node: " + t.getRoot().getData());
        System.out.println("Left child of root node " + t.getRoot().getData() + " is " + t.getRoot().getLeft().getData());
        System.out.println("Right child of root node " + t.getRoot().getData() + " is " + t.getRoot().getRight().getData());
        System.out.println("DEPTH : " + t.getRoot().getLeft().getLeft().getData() + " is " + t.depth(t.getRoot().getLeft().getLeft()) ) ;
        System.out.println("Depth of G (searching by value): " + t.depth(t.getRoot(), "G")) ;
        System.out.println("GET THE HEIGHT OF THE TREE  : " + t.height(t.getRoot()));
    }
}