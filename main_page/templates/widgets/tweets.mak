<div class='article'>
    <div class='author'></div>
    <div class='timeago' title='${x['title']}'></div>
    <br>

    <div class='content'>
        %if x['link']:
            <a href="${x['link']}"> ${x['link_name']} </a>
        %endif
    </div>
</div>
