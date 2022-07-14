// SPDX-License-Identifier: MIT
pragma solidity ^0.5.16;

contract contratoSuper {
    // variables globales -> (tipo de dato, visibilidad, nombre)
    //int public miValor;
    //variable[16]: variable formato array de longitud 16// hay 16 perros en adopcion y la variable address va almacenando las direcciones
    address[16] public perrosAdoptados;

    function adoptar(uint perroIndex) public returns (bool){
        // para poner condiciones existe la funcion require
        require( perroIndex >= 0 && perroIndex <= 15 , "Fuera de rango" );

        bool adoptarConExito = true;

        if ( perrosAdoptados[perroIndex] == address(0) ){
            // address deja de ser cero y se almacena en la variable perrosAdoptados - msg es una funcion que almacena datos
            perrosAdoptados[perroIndex] = msg.sender;
        }
        else {
            adoptarConExito = false;
        }
        return adoptarConExito;
    }

    function getPerrosAdoptados() public returns( address[16] memory ){
        // retorna una variable global, pero no modifica nada en la blockchain - son free- view function - memory funciona con array y con estructura de datos - no string no int
        return perrosAdoptados;

    }
}