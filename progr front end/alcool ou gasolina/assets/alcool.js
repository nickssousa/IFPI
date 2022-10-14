function app() {

    const cx_alcool = document.getElementById('cx_alcool')
    const cx_gasolina = document.getElementById('cx_gasolina')
    const cx_veiculo = document.getElementById('cx_veiculo')
    const cx_dinheiro = document.getElementById('cx_dinheiro')
    const cx_distancia = document.getElementById('cx_distancia')
    const btn_calcular= document.getElementById('btn_calcular')
    const btn_limpar= document.getElementById('btn_limpar')
    
    const resultado1= document.getElementById('resultado1')
    const resultado2 = document.getElementById('resultado2')
    const resultado3 = document.getElementById('resultado3')
    const resultado4 = document.getElementById('resultado4')
    

    btn_calcular.addEventListener('click', () =>{

        const distancia= Number(cx_distancia.value)
        const veiculo= Number(cx_veiculo.value)
        const precisa = distancia/ veiculo
        const precisa1= distancia/(veiculo*0.7) 

        resultado1.innerText= `Você irá precisar de ${precisa.toFixed(1)} litros de gasolina.`
        
        const gasolina = Number(cx_gasolina.value)*precisa

        resultado2.innerText= `O cobustível custará em torno de ${gasolina.toFixed(2)} reais.`

        const dinheiro = Number(cx_dinheiro.value)

        if (gasolina> dinheiro){
            resultado3.innerText= `Você precisará de ${(gasolina- dinheiro).toFixed(2)} R$ a mais para abastecer.`
        }else {
            resultado3.innerText= `Você receberá ${(dinheiro - gasolina).toFixed(2)} R$ de troco.`
        }
        
        const alcool = Number(cx_alcool.value)*precisa1

        resultado4.innerText= `Você irá precisar de ${(precisa1).toFixed(1)} litros de alcool.`
        resultado5.innerText= `O cobustível custará em torno de ${alcool.toFixed(2)} reais.`

        if (alcool> dinheiro){
            resultado6.innerText= `Você precisará de ${(alcool- dinheiro).toFixed(2)} R$ a mais para abastecer.`
        }else {
            resultado6.innerText= `Você receberá ${(dinheiro - alcool).toFixed(2)} R$ de troco.`
        }

    })

    btn_limpar.addEventListener('click', () =>{
        cx_alcool.value = ''
        cx_gasolina.value = ''
        cx_veiculo.value = ''
        cx_dinheiro.value= ''
        cx_distancia.value= ''

        resultado1.innerText = ''
        resultado2.innerText = ''
        resultado3.innerText = ''
        resultado4.innerText = ''
        resultado5.innerText = ''
        resultado6.innerText = ''

        cx_alcool.focus()

    })

}

app()