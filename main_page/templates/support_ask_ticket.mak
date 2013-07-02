<%include file="top.mak"/>
			<div id="main_page">
			<div id="left"> 
				<div id="nav">
					<ul>
						% for row in menu_left_list:
							<li><a href="${row[0]}" id="homenav">${row[1]}</a></li>
						% endfor
	    			</ul>
			 </div>
			</div>
				<div id="center" style="width:820px;">
					<div class="settings_container" style="width:800px;">
						<div class="settings_header">Ticket - ${ticket_num}</div>

<div class="clear listing">
  <table class="alws support" width="100%" cellspacing="0" cellpadding="4" border="0">
 <tbody><tr class="odd" onmouseout="this.className='odd'" onmouseover="this.className='highlight'">
  <td class="comment-meta" width="25%"><p class="meta">
 kamilx3@gmail.com
</p>
  </td>
  <td class="comment-body" width="75%">
<p class="meta right">21 Wrz 2010 à 17:38</p>
<a name="8445"></a>
<p>I'm trying to run this: http://www.ibm.com/developerworks/library/x-googleclndr/#c5 script, but I'm getting the "(...)Uncaught exception 'Zend_Gdata_App_HttpException' with message 'Unable to Connect to ssl://www.google.com:443(...)" error - I read that it possible that php.ini is not configured correctly, so I tried to change it, but it don't made the change ( maybe I did it wrong )... I will be grateful for any help.</p>
  </td>
 </tr>
 <tr class="even" onmouseout="this.className='even'" onmouseover="this.className='highlight'">
  <td class="comment-meta" width="25%"><p class="meta">
 kamilx3@gmail.com
</p>
  </td>
  <td class="comment-body" width="75%">
<p class="meta right">21 Wrz 2010 à 17:53</p>
<a name="8446"></a>
<p>You should add the openssl extension to your php.ini, in your panel : Environments &gt; PHP. But you should JUST add the new lines you want, not the whole php.ini file.</p>
<p>You can see the default file in your account, in /cgi-bin/</p>
  </td>
 </tr>
 <tr class="odd" onmouseout="this.className='odd'" onmouseover="this.className='highlight'">
  <td class="comment-meta" width="25%"><p class="meta">
 kamilx3@gmail.com
</p>
  </td>
  <td class="comment-body" width="75%">
<p class="meta right">21 Wrz 2010 à 20:33</p>
<a name="8448"></a>
<p>It is how I did it before pasting whole php.ini - I wrote only "extension=php_openssl.dll" but it does not work...</p>
  </td>
 </tr>
 <tr class="even" onmouseout="this.className='even'" onmouseover="this.className='highlight'">
  <td class="comment-meta" width="25%"><p class="meta">
 Cyril
</p>
  </td>
  <td class="comment-body" width="75%">
<p class="meta right">21 Wrz 2010 à 21:16</p>
<a name="bottom"></a>
<a name="8449"></a>
<p>You must have:</p>
<p>extension=openssl.so</p>
<p>as we're on Linux, not Windows.</p>
<p>Regards,</p>
  </td>
 </tr>
  </tbody></table>
 </div>

					</div>
				</div>
			</div>	
<%include file="bottom.mak"/>