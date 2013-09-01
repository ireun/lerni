
<div class="grid" id="grid" style="height: 518px;">

		<div class="inner">
						<div class="box welcome">
				<h1>Unheap</h1>
				<p>A tidy repository of <span>jQuery plugins</span></p>
				<ul>
					<li><a href="http://feeds.feedburner.com/unheap" class="feed">Get the feed<span></span></a></li>
					<li><a href="http://twitter.com/unheap" class="twitter">Follow us on Twitter<span></span></a></li>
					<li><a href="javascript:void(0)" class="share">Share Unheap<span></span></a></li>
				</ul>
			</div>
						<div class="box ad">
				<img src="http://www.unheap.com/wp-content/themes/unheap/imgs/ad-box.png" alt="">
			</div>

			<div class="box">
								
								<img src="http://www.unheap.com/wp-content/uploads/passy.png" alt="">
				<div class="inner-content">
					<h4><a href="http://www.unheap.com/inputs-forms/password/passy/" rel="bookmark" title="Passy">Passy</a></h4>
										<p>A &nbsp;plugin to help rate and generate passwords.</p>					<p class="full-desc">A &nbsp;plugin to help rate and generate passwords.</p>
					<a href="#" class="hide-full-desc">X</a>
				</div>
				<div class="author-twitter-handle" style="z-index: 0;"><a href="http://twitter.com/@timseverien" title="Author on Twitter" target="_blank">@timseverien</a></div>				<ul class="in-categories" style="z-index: 0;">
					<li>
						<a title="View all posts in Password" href="http://www.unheap.com/section/password/">Password</a>					</li>
				</ul>
				<div class="overlay" style="display: none;">
					<a href="http://www.unheap.com/?out=10864" class="button-launch" target="_blank">Launch</a>					<div class="plugin-stats" style="bottom: -33px;">
						<ul class="data">
														<li class="save-plugin"><a class="wpfp-link not-logged-in">Save</a></li>
							<li class="save-count">3</li>
						</ul>
						<ul class="sharing">
							<li class="views">
							333							</li>
							<li><a href="#" class="share">Share</a></li>
							<li><a href="http://www.unheap.com/feedback/?url=http://www.unheap.com/inputs-forms/password/passy/#bug" class="report-bug">Report bug</a></li>
						</ul>
					</div>
				</div>
			</div>
		</div>
</div>

.grid {
	overflow-y: visible;
	-ms-overflow-y: visible;
	overflow-x: hidden;
	margin: 49px 0 0 0; padding: 0 0 50px 0;

	/*display: none;*/
}

	.grid .inner {
		padding: 45px 0 0 45px;
	}

	.grid .box {
		background: #0e0e0e;
		-moz-border-radius: 6px;
		-webkit-border-radius: 6px;
		border-radius: 6px;
		width: 250px;
		height: 300px;
		margin: 0 2% 2% 0;
		float: left;
		overflow: hidden;
		position: relative;
	}

		.loading-hide {
			background: #000;
			width: 250px;
			height: 141px;
			position: absolute;
			top: 0; left: 0;
			z-index: 9999;
			-moz-transition: opacity 300ms ease-out;
			-webkit-transition: opacity 300ms ease-out;
			-ms-transition: opacity 300ms ease-out;
			transition: opacity 300ms ease-out;
		}

		.loading-hide.hide {
			opacity: 0;
		}

		.grid .box .post-edit-link {
			text-indent: -9999em;
			background: url(../imgs/box-edit-post.png) no-repeat;
			width: 11px;
			height: 11px;
			position: absolute;
			top: 15px; right: 13px;
		}

		.grid .box img {
			-moz-border-radius: 6px 6px 0 0;
			-webkit-border-radius: 6px 6px 0 0;
			border-radius: 6px 6px 0 0;
			width: 250px;
			height: 140px;
			float: left;
		}

		.grid .box .inner-content {
			background: #0e0e0e;
			padding: 20px 15px 0 15px;
			position: relative;
			z-index: 5;
			clear: both;
		}

		.grid .box .border-radius {
			-moz-border-radius: 6px;
			-webkit-border-radius: 6px;
			border-radius: 6px;
		}

			.box .inner-content h4 {
				height: 21px;
			}

			.box .inner-content h4 a {
				color: #d4d4d4;
				font-family: Gotham, "proxima-nova", "Helvetica Neue", Helvetica, Arial, sans-serif;
				font-size: 1.15em;
				letter-spacing: 0.1em;
				text-transform: uppercase;
			}

			.box .inner-content h4 a:hover {
				color: #00a5cb;
				text-decoration: none;
				border-bottom: 1px dotted #00a5cb;
			}

			.box .inner-content p {
				font-family: "proxima-nova", "Lucida Grande", "Helvetica Neue", Helvetica, Arial, sans-serif;
				color: #838383;
				font-size: 12px;
				line-height: 18px;
				height: 60px;
			}

			.box .inner-content .full-desc {
				margin: -60px 15px 0 0;
				position: absolute;
				display: none;
			}

			.box .inner-content .show-full-desc {
				text-indent: -9999em;
				background: url(../imgs/box-button-show.png) no-repeat;
				width: 33px;
				height: 9px;
				line-height: 9px;
				position: relative;
				display: inline-block;
			}

			.box .inner-content .hide-full-desc {
				text-indent: -9999em;
				background: url(../imgs/box-button-hide.png) no-repeat;
				width: 25px;
				height: 25px;
				margin: 100px auto 0 auto;
				display: none;
			}

			.box .inner-content .show-full-desc:hover,
			.box .inner-content .hide-full-desc:hover  {
				background-position: bottom left;
			}

		.grid .box .author-twitter-handle {
			background: url(../imgs/author-twitter-handle.png) no-repeat 0 3px;
			padding: 0 0 0 17px;
			position: absolute;
			bottom: 36px; left: 14px;
		}

			.grid .box .author-twitter-handle a {
				font-family: "Lucida Grande", "Lucida Sans Unicode", "Lucida Sans", Geneva, Verdana, sans-serif;
				color: #8bb8bb;
				font-size: 1.0em;
			}

			.grid .box .author-twitter-handle a:hover {
				color: #00cbdc;
				text-decoration: none;
			}

		.grid .box .in-categories {
			font-family: "Lucida Grande", "Lucida Sans Unicode", "Lucida Sans", Geneva, Verdana, sans-serif;
			background: url(../imgs/in-categories.png) no-repeat 0 3px;
			padding: 0 0 0 11px;
			position: absolute;
			bottom: 15px; left: 15px;
		}

			.grid .box .in-categories li {
				color: #595858;
				font-size: 0.90em;
				text-transform: uppercase;
				float: left;
			}

			.grid .box .in-categories li a {
				color: #595858;
				font-size: 1.2em;
				text-transform: none;
				margin: -3px 0 0 5px;
				display: inline-block;
			}

			.grid .box .in-categories li a:hover {
				color: #00cbdc;
				text-decoration: none;
			}

		.grid .box .badges {
			position: absolute;
			top: 116px; right: 0;
		}

			.grid .box .badges .badge-paid,
			.grid .box .badges .badge-spotlight,
			.grid .box .badges .badge-video {
				text-indent: -9999em;
				background: #35c97f url(../imgs/key-paid.png) no-repeat center;
				width: 29px;
				height: 24px;
				float: left;
			}

			.grid .box .badges .badge-spotlight {
				background: #ffbb00 url(../imgs/key-featured.png) no-repeat center;
			}

			.grid .box .badges .badge-video {
				background: #06afb8 url(../imgs/key-video.png) no-repeat center;
			}

		.grid .box .overlay {
			text-align: center;
			background: rgba(0, 222, 255, .25);
			-moz-border-radius: 6px 6px 0 0;
			-webkit-border-radius: 6px 6px 0 0;
			border-radius: 6px 6px 0 0;
			width: 250px;
			height: 141px;
			position: absolute;
			top: 0; left: 0;
			display: none;
		}

			.box .overlay .button-launch,
			.button-hold .button-launch {
				text-indent: -9999em;
				background: url(../imgs/overlay-button-launch.png) no-repeat;
				width: 92px;
				height: 26px;
				margin: 42px 3px 0 0;
				display: inline-block;
			}

			.box .overlay .button-demo,
			.button-hold .button-demo {
				text-indent: -9999em;
				background: url(../imgs/overlay-button-demo.png) no-repeat;
				width: 69px;
				height: 26px;
				display: inline-block;
			}

			.box .overlay .button-video {
				text-indent: -9999em;
				background: url(../imgs/overlay-button-video.png) no-repeat;
				width: 38px;
				height: 26px;
				margin: 0 0 0 3px;
				display: inline-block;
			}

			.box .overlay .button-launch:hover,
			.box .overlay .button-demo:hover,
			.box .overlay .button-video:hover,
			.button-hold .button-launch:hover,
			.button-hold .button-demo:hover {
				background-position: 0 -26px;
			}

			.box .overlay .plugin-stats {
				text-align: left;
				background: #ffe200;
				border-top: 1px solid #fff100;
				width: 250px;
				height: 33px;
				position: absolute;
				left: 0; bottom: -33px;
				/*left: 0; bottom: 0;*/
				z-index: 1;
			}

				.box .overlay .plugin-stats .data {
					margin: 0 0 0 10px;
					float: left;
				}

					.box .overlay .plugin-stats li {
						color: #695902;
						font-size: 1.2em;
						font-weight: bold;
						padding: 1px 0;
						float: left;
					}

					.box .overlay .plugin-stats .save-plugin {
						width: 63px;
					}

					.box .overlay .plugin-stats .save-plugin a {
						color: #ffe200;
						font-size: 1.1em;
						font-weight: bold;
						text-align: center;
						background: #ac9307;
						-moz-border-radius: 3px;
						-webkit-border-radius: 3px;
						border-radius: 3px;
						width: 50px;
						height: 20px;
						line-height: 20px;
						margin: 5px 12px 0 0;
						display: inline-block;
						position: relative;
						-moz-transition: .3s ease-in-out;
						-webkit-transition: .3s ease-in-out;
						transition: .3s ease-in-out;
					}

					.box .overlay .plugin-stats .save-plugin a:hover {
						text-decoration: none;
						background: #6e5f09;
					}

					.box .overlay .plugin-stats a.remove-saved {
						background: #6e5f09;
					}

					.box .overlay .plugin-stats a.remove-saved:after {
						left: 100%;
						border: solid transparent;
						content: " ";
						height: 0;
						width: 0;
						position: absolute;
						pointer-events: none;
						-moz-transition: .3s ease-in-out;
						-webkit-transition: .3s ease-in-out;
						transition: .3s ease-in-out;
					}

					.box .overlay .plugin-stats a.remove-saved:after {
						border-color: rgba(110, 95, 9, 0) !important;
						border-left-color: #6e5f09 !important;
						border-width: 5px;
						top: 50%;
						margin-top: -5px;
					}

					.box .overlay .plugin-stats .save-plugin a:after {
						left: 100%;
						border: solid transparent;
						content: " ";
						height: 0;
						width: 0;
						position: absolute;
						pointer-events: none;
					}

					.box .overlay .plugin-stats .save-plugin a:after {
						border-color: rgba(172, 147, 7, 0);
						border-left-color: #ac9307;
						border-width: 5px;
						top: 50%;
						margin-top: -5px;
						-moz-transition: .3s ease-in-out;
						-webkit-transition: .3s ease-in-out;
						transition: .3s ease-in-out;
					}

					.box .overlay .plugin-stats .save-plugin a:hover:after {
						left: 100%;
						border: solid transparent;
						content: " ";
						height: 0;
						width: 0;
						position: absolute;
						pointer-events: none;
					}

					.box .overlay .plugin-stats .save-plugin a:hover:after {
						border-color: rgba(110, 95, 9, 0);
						border-left-color: #6e5f09;
						border-width: 5px;
						top: 50%;
						margin-top: -5px;
					}

					.box .overlay .plugin-stats .save-count {
						color: #695902;
						font-weight: bold;
						padding: 9px 0 0 0;
					}

					.box .overlay .plugin-stats .views {
						background: url(../imgs/overlay-views.png) no-repeat 0 3px;
						padding: 2px 0 0 30px;
						text-align: right;
					}

				.box .overlay .plugin-stats .sharing {
					height: 19px;
					margin: 7px 0 0 0; padding: 0 0 0 12px;
					float: right;
				}

					.box .overlay .sharing li {
						margin: 0 12px 0 0;
						float: left;
					}

						.box .overlay .sharing li .related {
							text-indent: -9999em;
							background: url(../imgs/overlay-related.png) no-repeat;
							width: 17px;
							height: 11px;
							margin: 3px 0 0 0;
							display: block;
							opacity: .59;
						}

						.box .overlay .sharing li .share {
							text-indent: -9999em;
							background: url(../imgs/overlay-share.png) no-repeat;
							width: 20px;
							height: 13px;
							margin: 2px 0 0 0;
							display: block;
							opacity: .59;
						}

						.box .overlay .sharing li .report-bug {
							text-indent: -9999em;
							background: url(../imgs/overlay-report-bug.png) no-repeat;
							width: 16px;
							height: 14px;
							margin: 2px 0 0 0;
							display: block;
							opacity: .59;
						}

						.box .overlay .sharing li a:hover {
							opacity: 1;
						}

		.grid .welcome {
			text-align: center;
		}

			.grid .welcome h1 {
				text-indent: -9999em;
				background: url(../imgs/welcome-logo.png) no-repeat;
				width: 129px;
				height: 47px;
				margin: 35px 0 16px 0;
				display: inline-block;
			}

			.grid .welcome p {
				font-family: "Book Antiqua", Palatino, "Palatino Linotype", "Palatino LT STD", Georgia, serif;
				color: #878787;
				font-size: 1.7em;
				font-style: italic;
				line-height: 23px;
			}

				.grid .welcome p span {
					color: #bdbdbd;
					display: block;
				}

			.grid .welcome ul {
				text-align: left;
				margin: 30px 0 0 0;
			}

				.grid .welcome li {
					border-top: 1px solid #212121;
					line-height: 33px;
					margin: 0 20px;
				}

					.grid .welcome li a {
						-moz-transition: all .3s ease-in-out;
						-webkit-transition: all .3s ease-in-out;
						transition: all .3s ease-in-out;
						position: relative;
					}

					.grid .welcome li a:hover {
						color: #b2c0c0;
						text-decoration: none;
					}

					.grid .welcome li a:hover span {
						opacity: 1;
					}

					.grid .welcome li a span {
						opacity: 0;
						position: absolute;
						top: 0; left: 0;
						-moz-transition: all .3s ease-in-out;
						-webkit-transition: all .3s ease-in-out;
						transition: all .3s ease-in-out;
					}

					.grid .welcome .feed {
						color: #ff6c00;
						font-family: "proxima-nova","Proxima Nova", "Lucida Grande", "Helvetica Neue", Helvetica, Arial, sans-serif;
						font-size: 1.4em;
						font-weight: 700;
						background: url(../imgs/welcome-box-social.png) no-repeat 0 2px;
						margin: 0 20px 0 46px; padding: 0 0 0 25px;
					}

						.grid .welcome .feed span {
							background: #0e0e0e url(../imgs/welcome-box-social.png) no-repeat -5px -90px;
							width: 11px;
							height: 11px;
							margin: 2px 0 0 5px;
						}

					.grid .welcome .twitter {
						color: #02acd6;
						font-family: "proxima-nova","Proxima Nova", "Lucida Grande", "Helvetica Neue", Helvetica, Arial, sans-serif;
						font-size: 1.4em;
						font-weight: bold;
						background: url(../imgs/welcome-box-social.png) no-repeat 0 -23px;
						margin: 0 20px 0 20px; padding: 0 0 0 30px;
					}

						.grid .welcome .twitter span {
							background: #0e0e0e url(../imgs/welcome-box-social.png) no-repeat 0 -115px;
							width: 19px;
							height: 12px;
							margin: 2px 0 0 0;
						}

					.grid .welcome .share {
						color: #b783fd;
						font-family: "proxima-nova","Proxima Nova", "Lucida Grande", "Helvetica Neue", Helvetica, Arial, sans-serif;
						font-size: 1.4em;
						font-weight: bold;
						background: url(../imgs/welcome-box-social.png) no-repeat 0 -45px;
						margin: 0 20px 0 41px; padding: 0 0 0 30px;
					}

						.grid .welcome .share span {
							background: #0e0e0e url(../imgs/welcome-box-social.png) no-repeat 0 -135px;
							width: 19px;
							height: 14px;
						}

			.grid .ad {
				background: #000;
			}

				.grid .ad img {
					margin: 40px 0 0 27px;
				}

	.grid .pagination {
		float: left;
		clear: both;
	}