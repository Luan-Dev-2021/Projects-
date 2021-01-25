setInterval(() => {
    pp = document.querySelector("#react-root > section > main > div > header > section > ul > li:nth-child(3) > a");
    pp.click();
    cont = 0;
    let contador = 0;

    document.querySelectorAll('._0imsa').forEach((item, index) => {
        var lu = item.innerText;
        var tt = item.index;
        contador++;
        //console.log(contador);
        //console.log(lu);
        var ly = (contador + ',' + lu);
		
        if (ly.indexOf('digite o nome que quer deixar de seguir') !== -1) {
            cont = 1;
            clearInterval();
            var lp = new String(ly);
            //console.log(lp);
            output = lp.split(",");
            var fm = output[0]
            console.log(fm);
            try {
                bt = document.querySelector(`body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(${fm}) > div > div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button`);
                bt.click();
            } catch (e) {
                if (e instanceof TypeError) {
                    // declarações para manipular exceções TypeError
                    console.log("deu certo");
                    var oo = document.querySelector(`body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(${fm}) > div > div.Pkbci > button`);
                    oo.click();
                }
            }

        }
        if (cont == 0) {
            x = document.querySelector('.isgrP');
            x.scrollTop += 300;
            x.scrollTop += 300;
        }
    })
}, 5000)