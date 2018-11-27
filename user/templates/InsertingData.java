import java.io.*;
import java.lang.*;
import java.sql.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class InsertingData extends HttpServlet{
  public void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
    response.setContentType("text/html");
    PrintWriter out = response.getWriter();
        try{
      String name = request.getParameter("c_name");
      String mail = request.getParameter("c_mail");
      String sub = request.getParameter("c_sub");
      String msg = request.getParameter("c_msg");
      out.println(name);
      out.println(mail);
      out.println(sub);
      out.println(msg);
      Class.forName("com.mysql.jdbc.Driver");
Connection con=DriverManager.getConection("jdbc:mysql://localhost:3306/contact","root","");
      PreparedStatement pst = con.prepareStatement("insert into form_c values(?,?,?,?)");
      pst.setString(1,name);
      pst.setString(2,mail);
      pst.setString(3,sub);
      pst.setString(4,msg);
      int i = pst.executeUpdate();
      if(i!=0){
        out.println("<br>Record has been inserted");
      }
      else{
        out.println("failed to insert the data");
      }
    }
    catch (Exception e){
      out.println(e);
    }
  }
}