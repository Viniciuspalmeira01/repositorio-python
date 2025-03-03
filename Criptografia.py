{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPenZVmvnPHqBCDJQ8H3n00",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Viniciuspalmeira01/Projeto-um/blob/main/Criptografia.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *Projetos milabola*"
      ],
      "metadata": {
        "id": "stnTMi2e97hv"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "zH4IXKtCT_5B"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "XYa1DkHvI21A"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class Broken:\n",
        "    def __init__(self) -> None:\n",
        "        self.alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']\n",
        "        self.number_letras = len(self.alfabeto)\n",
        "\n",
        "    def Criptografar(self, palavra):\n",
        "        lista = list(palavra)\n",
        "        x = 0\n",
        "        tam = len(lista)\n",
        "        for i in range(tam):\n",
        "            x += i\n",
        "            x_str = str(x)\n",
        "            lista[i] = x_str  # Substitui a letra pelo número\n",
        "\n",
        "        new_palavra = \"\".join(lista)\n",
        "        return new_palavra  # Retorna a string criptografada\n",
        "\n",
        "    def Decriptografar(self, cripto):\n",
        "        cripto = str(cripto)  # Converter número para string\n",
        "        lista = list(cripto)\n",
        "        tam = len(lista)\n",
        "        x = 0\n",
        "\n",
        "        for i in range(tam):\n",
        "            x += i\n",
        "            index = x % len(self.alfabeto)  # Garante que o índice esteja dentro do alfabeto\n",
        "            lista[i] = self.alfabeto[index]\n",
        "\n",
        "        return \"\".join(lista)  # Retorna a string descriptografada\n",
        "\n",
        "# Testando\n",
        "auto = Broken()\n",
        "criptografado = auto.Criptografar(\"Vasco\")\n",
        "print(f\"Criptografado: {criptografado}\")\n",
        "\n",
        "descriptografado = auto.Decriptografar(criptografado)\n",
        "print(f\"Descriptografado: {descriptografado}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8ZYO6hgx-GXI",
        "outputId": "293f787c-1802-4327-8bdb-3df9fa34f92b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Criptografado: 013610\n",
            "Descriptografado: abdgkp\n"
          ]
        }
      ]
    }
  ]
}