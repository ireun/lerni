                        </td>
                    </tr>
					<tr>
						<td bgcolor="#ee4c50" style="padding: 30px 30px 30px 30px;">
							<table border="0" cellpadding="0" cellspacing="0" width="100%">
								<tr>
									<td style="color: #ffffff; font-family: Arial, sans-serif; font-size: 14px;" width="75%">
										&reg; ${copy_right}<br/>
                                        %if unsubscribe:
										<a href="${unsubscribe}" style="color: #ffffff;"><font color="#ffffff">Unsubscribe</font></a> to this newsletter instantly
                                        %endif
									</td>
                                    %if twitter:
                                        <td style="font-family: Arial, sans-serif; font-size: 12px; font-weight: bold;">
                                            <a href="http://www.twitter.com/${twitter[1]}" style="color: #ffffff;">
                                                <img src="${twitter[0] | n}" alt="Twitter" width="38" height="38" style="display: block;" border="0" />
                                            </a>
                                        </td>
                                    %endif
                                    %if twitter and facebook:
                                        <td style="font-size: 0; line-height: 0;" width="20">&nbsp;</td>
                                    %endif
                                    %if facebook:
                                        <td style="font-family: Arial, sans-serif; font-size: 12px; font-weight: bold;">
                                            <a href="http://www.facebook.com/${facebook[1]}" style="color: #ffffff;">
                                                <img src="${facebook[0] |n}" alt="Facebook" width="38" height="38" style="display: block;" border="0" />
                                            </a>
                                        </td>
                                    %endif
								</tr>
							</table>
						</td>
					</tr>
				</table>
			</td>
		</tr>
	</table>
</body>
</html>