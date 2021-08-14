# in this file you will find all pathes that F4T3H-C2 tool deal with.
# you can change any value here, but be careful when you do any change at variable names :).

from getpass import getuser # to get curranr loged in username.



# Default shell exporting path, any new shell will be generated in this path.
DEF_SHELL_PATH = f"/home/{getuser()}/Desktop/"


# Server-Root path (for sending files), the following path will be available for anyone (target)
# who will try to access it by the URL.
UPLOADING_SERVER_ROOT_PATH = f"/home/{getuser()}/Desktop/"


# Default download path, any file you will get from the target machine, you will find it here:
DESKTOP_PATH = f"/home/{getuser()}/Desktop/"


# CSS code for geoip class
CSS_CODE = """
<style>
    h1{
      font-size: 25px;
      color: #fff;
      text-transform: uppercase;
      font-weight: 200;
      text-align: center;
      margin-bottom: 10px;
    }

    table{
      width:100%;
      table-layout: fixed;
    }

    .tbl-header{
      background-color: rgba(255,255,255,0.3);
    }

  .tbl-content{
    height:400px;
    overflow-x:auto;
    margin-top: 0px;
    border: 1px solid rgba(255,255,255,0.3);
  }

  th{
    padding: 15px 10px;
    text-align: left;
    font-weight: 200;
    font-size: 16px;
    color: #fff;
    text-transform: uppercase;
  }

  td{
    padding: 10px;
    text-align: left;
    vertical-align:middle;
    font-weight: 200;
    font-size: 16px;
    color: #fff;
    border-bottom: solid 1px rgba(255,255,255,0.1);
  }

  /* demo styles */
  @import url(https://fonts.googleapis.com/css?family=Roboto:400,500,300,700);
  body{
    background: -webkit-linear-gradient(left, #0b1d16, #2d5558);
    background: linear-gradient(to right, #0b1d16, #2d5558);
    font-family: 'Roboto', sans-serif;
  }

  section{
    margin: 50px;
  }
</style>
"""


# Table code for geoipclass
HTML_TABLE_CODE = """
<section>
    <!--for demo wrap-->
<div class="tbl-header">
<table cellpadding="0" cellspacing="0" border="0">
 <thead>
   <tr>
     <th>[+] All About <span style= "color:red;"> {0} </span></th>
   </tr>
 </thead>
</table>

</div>
<div class="tbl-content">
<table cellpadding="0" cellspacing="0" border="0">
 <tbody>

    <tr>
     <td>Country </td>
     <td>{1}</td>
    </tr>

    <tr>
     <td>City </td>
     <td>{2}</td>
    </tr>

    <tr>
     <td>Region </td>
     <td>{3}</td>
    </tr>

    <tr>
     <td>Region Code </td>
     <td>{4}</td>
    </tr>

    <tr>
     <td>Country Capital </td>
     <td>{5}</td>
    </tr>

    <tr>
     <td>Longitude </td>
     <td>{6}</td>
    </tr>

    <tr>
     <td>Latitude </td>
     <td>{7}</td>
    </tr>

    <tr>
     <td>Time Zone </td>
     <td>{8}</td>
    </tr>

    <tr>
     <td>Country Calling Code </td>
     <td>{9}</td>
    </tr>

    <tr>
     <td>Currency </td>
     <td>{10}</td>
    </tr>

    <tr>
     <td>Currency Name </td>
     <td>{11}</td>
    </tr>

    <tr>
     <td>Country Language </td>
     <td>{12}</td>
    </tr>

    <tr>
     <td>Country Area (KM) </td>
     <td>{13}</td>
    </tr>

    <tr>
     <td>Country Population (Person) </td>
     <td>{14}</td>
    </tr>

    <tr>
     <td>Asn </td>
     <td>{15}</td>
    </tr>

    <tr>
     <td>ISP-ORG </td>
     <td>{16}</td>
    </tr>
 </tbody>
</table>
</div>
</section>
"""




# TODO: improve this file generally

