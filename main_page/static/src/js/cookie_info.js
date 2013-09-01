head.js(jquery, jquery_cookie, function() {
	$(document).ready(function(){
		$.cookieCuttr({
		cookieAnalyticsMessage: "Ta strona używa ciasteczek (mniam, mniam, mniam)",
		cookieAcceptButtonText: "Rozumiem",
		cookieWhatAreLinkText: "A co to są ciasteczka?",
		cookieWhatAreTheyLink: "http://wszystkoociasteczkach.pl/",
		cookiePolicyLink: "/privacy-policy/#cookies" });	
	});
});