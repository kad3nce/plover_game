var MAX=$(".content_block").length;
      var current_block = -1;
      var wordCount=0;
      $(document).ready(function() {
          for(i=1;i<=MAX;i++){
            $("#block_"+i).hide()
            $(".lyrics_block").each(function(){
                block_text = $(this).text();
                words = block_text.split(" ");
                wordCount += words.length;
              });
          }
          console.log(wordCount);
          function getMatchResult(){
              users_text = $("#user_input").val();
              $("#user_input").val("");
              var currentText = $("#block_"+(current_block-1)+ " > .lyrics_block").text()
              //console.log(currentText);
              if($.trim(users_text).toLowerCase() == $.trim(currentText).toLowerCase()){
                //Correct!
                return "green";
              } else {
                //Not correct
		if(currentText == "Get ready!!!"){
		    return "green"
		} else {
                    return "red";
		}
              }

              //console.log(someText);
          }
          function cycler(){
              var rawTime = $("#block_"+(current_block)+" > .time").text();
              mins = parseInt(rawTime.slice(0,2), 10);
              secs = parseInt(rawTime.slice(3,5), 10);
              millis = parseInt(rawTime.slice(6,25), 10);

              timeOffset = (mins * 60 * 1000) + (secs * 1000) + millis;
              console.log(timeOffset);

              var nextRawTime = $("#block_"+(current_block+1)+" > .time").text();
              nextMins = parseInt(nextRawTime.slice(0,2), 10);
              nextSecs = parseInt(nextRawTime.slice(3,5), 10);
              nextMillis = parseInt(nextRawTime.slice(6,25), 10);

              nextTimeOffset = (nextMins * 60 * 1000) + (nextSecs * 1000) + nextMillis;
              console.log(nextTimeOffset);

              delta = nextTimeOffset - timeOffset;

              console.log(delta);
              //$("#block_"+current_block).delay(delta).hide(200);

              if(!isNaN(delta)){
                setTimeout( function() {
                  //hide old block
                  //Turn text grey, highlight background green or red based on correctness
                  //show upcoming block
                  //increment current block id
                  current_block +=1;
                  $("#block_"+(current_block-2)).hide(200);
                  $("#block_"+(current_block-1)).css("color", "lightgrey").css("font-size", "12pt").css("background", getMatchResult());
                  $("#block_"+(current_block)).css("color", "black").css("font-weight", "bold").css("font-size", "24pt");
                  $("#block_"+(current_block+1)).show(200).css("color", "lightgrey");
                  cycler();
                }, delta);
              }
          }
          $("#start_button").click(function() {
            cycler();
            $("#audio").get(0).play();
            $("#user_input").focus();
          });
          $("#user_input").keypress(function(e) {
            code= (e.keyCode ? e.keyCode : e.which);
            if (code == 13) {
              e.preventDefault();
            }
          });
      });

