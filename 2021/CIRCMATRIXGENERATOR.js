
// import { saveAs } from 'file-saver';

function summcount() {
	var k = parseInt(document.getElementById('input_k').value);
	var n = document.getElementById('input_n').value; n = n.split(document.getElementById('input_s').value); n = n.length - 1;
	document.getElementById('input_summcount').value = factorial(n) / factorial(k) / factorial(n - k);

}

function factorial(n) {
	if (n == 0)
		return 1;
	else
		return n * factorial(n - 1);
}
//document.getElementById('pokus').focus();

var tabla = document.createElement("div");

function MAXIMAGENERATOR() {

	tabla = document.createElement('div');

	var c = new Array();
	var s = document.getElementById('input_s').value;

	var nmassiv = document.getElementById('input_n').value;
	var nmassiv = nmassiv.split(s);
	var n = nmassiv.length - 1;

	var textstart1 = document.getElementById('text_start1').value;
	var textstart2 = document.getElementById('text_start2').value;
	var textmid1 = document.getElementById('text_mid1').value;
	var textmid2 = document.getElementById('text_mid2').value;
	var textend1 = document.getElementById('text_end1').value;
	var textend2 = document.getElementById('text_end2').value;

	var inkrestart = false; if (document.getElementById('inkre_start').checked) { inkrestart = true };
	var inkremid = false; if (document.getElementById('inkre_mid').checked) { inkremid = true };
	var inkreend = false; if (document.getElementById('inkre_end').checked) { inkreend = true };

	var k = parseInt(document.getElementById('input_k').value);

	var iism0;
	var ignoriism = false;
	var ignorthis = false;
	if (document.getElementById('ignor_iism').checked) {
		ignoriism = true;
		iism0 = document.getElementById('input_iism0').value;
		iism0 = iism0.split(',');
	}

	var iism1 = parseInt(document.getElementById('input_iism1').value);
	var iism2 = parseInt(document.getElementById('input_iism2').value);
	var out1 = parseInt(document.getElementById('input_out1').value);
	var out2 = parseInt(document.getElementById('input_out2').value);

	for (var i = 1; i <= k; i++) { c[i] = i; }
	var inkrement = 1;

	addPrefixForNomer(out1);
	if (inkrement >= out1 && inkrement <= out2) {

		printc(c, k, nmassiv, iism1, iism2, textstart1, textstart2, textmid1, textmid2, textend1, textend2, inkrestart, inkremid, inkreend, inkrement, iism0, ignoriism, ignorthis, out1, out2)
	}

	while (c[1] < n - k + 1) {
		i = k;

		while (c[i] + k - i + 1 > n) { i-- }


		c[i]++;

		for (var j = i + 1; j <= k; j++) { c[j] = c[j - 1] + 1; }
		inkrement++;
		if (inkrement >= out1 && inkrement <= out2) {
			printc(c, k, nmassiv, iism1, iism2, textstart1, textstart2, textmid1, textmid2, textend1, textend2, inkrestart, inkremid, inkreend, inkrement, iism0, ignoriism, ignorthis, out1, out2);
		}
	}

	addSuffixForNomer(out1, out2);

	var tablaText = tabla.innerText;
	var blob = new Blob([tablaText], { type: "text/plain;charset=utf-8" });
	saveAs(blob, "batchStuff.txt");
}

function addPrefixForNomer(out1) {
	var texta = document.createElement('text');
	var printAppend = "file_output_append:true;\n";
	texta.innerHTML = "nomer:" + out1 + ";\n";
	tabla.appendChild(texta);
}

function addSuffixForNomer(out1, out2) {
	var texta = document.createElement('text');
	var part1 = "et : sconcat(round(float((absolute_real_time()-starttime)/60)) , \" minutes\");\n";
	var part2 = "write_data(et, \"output-" + out1 + "-" + out2 + ".txt\");";
	texta.innerHTML = part1 + part2;
	tabla.appendChild(texta);
}

function printc(c, k, nmassiv, iism1, iism2, textstart1, textstart2, textmid1, textmid2, textend1, textend2, inkrestart, inkremid, inkreend, inkrement, iism0, ignoriism, ignorthis, out1, out2) {
	printstarttext(textstart1, textstart2, inkrestart, inkrement);

	// var tabla = document.getElementById('tabladiv');

	for (var iism = iism1; iism <= iism2; iism++) {

		if (ignoriism == true) {
			var j = 0;
			while (j < iism0.length) {
				j++;

				if (iism == parseInt(iism0[j])) {
					ignorthis = true; break;
				}
			}
		}

		if (ignorthis == false) {

			var lskoba = document.createElement('text');
			lskoba.innerHTML = '[';
			tabla.appendChild(lskoba);

			for (var i = 1; i <= k; i++) {


				if (i < k) {

					var texta = document.createElement('text');
					texta.innerHTML = nmassiv[c[i]] + '' + iism + ',';
					tabla.appendChild(texta);

				}
				else if (i == k && iism < iism2) {

					var texta = document.createElement('text');
					texta.innerHTML = nmassiv[c[i]] + '' + iism + '],';
					tabla.appendChild(texta);

				}
				else if (i == k && iism == iism2) {

					var texta = document.createElement('text');
					texta.innerHTML = nmassiv[c[i]] + '' + iism + ']';
					tabla.appendChild(texta);

				}

			}
			var br = document.createElement('text');
			//br.innerHTML='<br>'; //матрица разбита на строки если комент снят
			tabla.appendChild(br);

		} else if (ignorthis == true) { ignorthis = false }

	}
	printmidtext(textmid1, textmid2, inkremid, inkrement);
	printendtext(out1, out2, textend1, textend2, inkreend, inkrement);


}

function printstarttext(textstart1, textstart2, inkrestart, inkrement) {

	var textix = document.getElementById('text_start1').value;
	var texta = document.createElement('text');
	texta.innerHTML = textix;
	tabla.appendChild(texta);

	if (inkrestart == true) {
		var textix = inkrement;
		var texta = document.createElement('text');
		texta.innerHTML = textix;
		tabla.appendChild(texta);

	}


	var textix = textstart2;
	var texta = document.createElement('text');
	texta.innerHTML = textix;
	tabla.appendChild(texta);

}

function printmidtext(textmid1, textmid2, inkremid, inkrement) {

	// var tabla = document.getElementById('tabladiv');
	var textix = textmid1;
	var texta = document.createElement('text');
	texta.innerHTML = textix;
	tabla.appendChild(texta);


	if (inkremid == true) {
		var textix = inkrement;
		var texta = document.createElement('text');
		texta.innerHTML = textix;
		tabla.appendChild(texta);

	}


	var textix = textmid2;
	var texta = document.createElement('text');
	texta.innerHTML = textix;
	tabla.appendChild(texta);


}

function printendtext(out1, out2, textend1, textend2, inkreend, inkrement) {

	// var tabla = document.getElementById('tabladiv');
	var textix = textend1;
	var texta = document.createElement('text');
	texta.innerHTML = textix;
	tabla.appendChild(texta);

	if (inkreend == true) {
		var textix = inkrement;
		var texta = document.createElement('text');
		texta.innerHTML = textix;
		tabla.appendChild(texta);

	}


	var textix = textend2;
	var texta = document.createElement('text');
	var writeData = "write_data([nomer, %], \"output-" + out1 + "-" + out2 + ".txt\")$ nomer:nomer+1$\n";
	texta.innerHTML = textix + writeData;
	tabla.appendChild(texta);

}

function increase2000() {
	var min = document.getElementById("input_out1").value;
	var minVal = parseInt(min);
	document.getElementById("input_out1").value = minVal + 2000;
	document.getElementById("input_out2").value = minVal + 3999;
}

function decrease2000() {
	var min = document.getElementById("input_out1").value;
	var minVal = parseInt(min);
	document.getElementById("input_out1").value = minVal - 2000;
	document.getElementById("input_out2").value = minVal - 1;
}