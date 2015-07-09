document.write('<p class="rubrikLarge">PanGeoX</p>\
<p><i>Panorama Geodata eXtractor</i> is based on standard trigonometry, and created by <a href="http://geosupportsystem.wordpress.com">Klas Karlsson</a>. It uses <a href="http://leafletjs.com">LeafletJS</a> for visible work with panoramas and maps. In the background it uses <a href="https://github.com/jseidelin/exif-js">ExifJS</a> and <a href="http://proj4js.org">Proj4JS</a> as well. To visualize panoramas <a href="http://pannellum.org">Pannellum</a> is used.</p>\
<p>All necessary files are included in the "package", no installation needed.</p>\
<p class="rubrikSmall">Requirements</p>\
<p>Panoramas need to be 360&deg; horisontal and for "measurements" they are assumed to cover 180&deg; vertically.<br>The only other <u>requirement</u> is that the edge of the panorama is oriented to grid north (not magnetic or true).</p>\
<p id="explained"><i>grid north = true north - c<br>c = atan(tan(Longitude - center meridian) * sin(Latitude))<br><br>\
c = atan( tan(<input type="text" size="1" id="LO" value="Lon" onchange="calcC()">-<input type="text" size="1" id="CM" value="CM" onchange="calcC()">) * sin(<input type="text" size="1" id="LA" value="Lat" onchange="calcC()">) = <input type="text" size="1" id="C">&deg;</i><br>\
<small><br>(Honestly all these calculations and "convergences" are confusing and makes my head hurt, please be careful!)</small></p>\
<img src="pangeox_resources/helpEditPanorama.png" class="helpImage">\
<p>Due to restrictions in JavaScript the application files need to reside in the same folder as the created panoramas. Use the package and un-zip in the panoramafolder.</p>\
<p><img src="pangeox_resources/helpFirefox.png" class="smallLeftAlign">To use Pannellum to view panoramas you need Firefox, or a web server (with a modern  WebGL browser, like Firefox). You can start a mini-web server with python from the panorama folder:</p>\
<i>python -m SimpleHTTPServer</i>\
<p>Then use the url: <a href="http://localhost:8000/pangeox.html">http://localhost:8000/pangeox.html</a></p>\
<p>To use the pre-configured Open Street Map background, Internet access is required. You can edit the source code to use local OGC web maps if you need to.</p>\
<p>For full functionality you need a connected mouse and access to your file-system, which makes the application less suitable for phones and tablets.</p>\
<p class="rubrikSmall">GPS tags</p>\
<p>The application can read EXIF GPS data from the panoramas, but you can also edit positions manually. It is however highly recommended that you use EXIF.<br>You can use <a href="http://www.sno.phy.queensu.ca/~phil/exiftool/">ExifTool</a> to set the position in a terminal:</p>\
<i>exiftool -GPSLatitude="57 deg 39\' 55.9\'\' N" -GPSLongitude="14 deg 58\' 20.6\'\' E" "panorama.jpg"</i>\
<p class="rubrikSmall">Measurements</p>\
<p>It is possible to make very simple measurements in the panoramas.</p>\
<p>When a location has been established you get distance to the location in each panorama, and a link that enables "Measurement Mode".</p>\
<p>The selected location is used as a reference point for your measurements in Measurement Mode, and measurements are done by one important assumption:</p>\
<p>The measured distance is assumed to be perpendicular to the viewing angle for the reference point (or the target point).</p>\
<img src="pangeox_resources/helpMeasure.png" class="helpImage"><br>\
<p>Height measurements are based on the same principles as above.</p>\
<p>Values outside parenthesis are perpendicular to the reference point, and values inside parenthesis are perpendicular to the target point.</p>\
<p>These measurements are <u>not</u> reliable, but can be used as an indication of size.</p>\
<p>It is not possible to measure distances in objects with high degree of perspective with this method!</p>\
\
<p class="rubrikSmall">Why UTM?</p>\
<p>Angular calculations and measurements could be done with latitude and longitudes, but it was easier for me to get distances in meters and doing trigonometry when I used a projected system.</p>\
<p>The disadvantage is that you need to consider this when you reference your images to the north! The north reference should be "grid" north as opposed to magnetic or true.</p>\
<p>Panoramas on the UTM boundary line, may be a cause for problems. Try to use pairs of panoramas that are in the same UTM zone.</p>\
<p class="rubrikSmall">Why a csv-file?</p>\
<p><ol><li>Small size</li><li>Human readable</li><li>Easy to use in GIS</li><li>Simple!</li></ol></p>\
<p class="rubrikSmall">Accuracy</p>\
<p>The accuracy of the objects in your list is highly depending on the accuracy of your panoramas and their GPS-location. More critical though is the panorama orientation to grid north. By being thorough it\'s possible to achieve reasonably high accuracy in your object locations, but never higher than the accuracy of your tools.</p>\
<p>A smart phone may create "pretty" panoramas, but the GPS and Compass inaccuracy may result in very low accuracy object locations. You should always verify your data by other means before use.</p>\
<p>If you have low accuracy in your panoramas, you will get low to very low accuracy in your objects and measurements.</p>\
<p class="rubrikSmall">Disclaimer</p>\
<p>PanGeoX is a non-profit application and I take no responsibility for the accuracy in the resulting data, or any other problems that the use of the application may lead to.</p><p>You are yourself solely responsible for all derived data and how the application is used.</p>\
<p><i>This is so stupidly obvious, but it clearly needs to be stated. I will of course try my best to get the application to work as good as possible, but I can never give any guarantees.</i></p>\
');
