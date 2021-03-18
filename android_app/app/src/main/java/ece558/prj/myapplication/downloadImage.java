package ece558.prj.myapplication;

public class downloadImage{
    public String name;
    public String url;
    public downloadImage (){
    }
    public downloadImage(String name, String url) {
        this.name = name;
        this.url = url;
    }
    public String getName() {
        return name;
    }
    public String getUrl() {
        return url;
    }
}
