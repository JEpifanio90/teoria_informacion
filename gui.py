from Tkconstants import END
from Tkinter import Tk, W, E, N, Text, HORIZONTAL, DISABLED, NORMAL, INSERT, StringVar
import os
from ttk import Frame, Button, Label, Style
from ttk import Entry, Separator
from elemental_coding import ElementalCoding
from huffman import HuffmanCoding
from interval_coding import interval_coding, arithmetic_intervals, elias_intervals
from lzw import DictionaryCoding
import diccionario as dic


def get_file_contents(file_path):
    with open(file_path) as file_to_exctract_contents:
        contents = file_to_exctract_contents.read()
    return contents

class ElementalCodingGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.elemental_coding = ElementalCoding()
        self.huffman_coding = HuffmanCoding()
        self.dictionary_coding = DictionaryCoding()
        self.init_ui()
        self.current_encoding = 5

    def init_ui(self):
        self.parent.title("Information Theory")
        Style().configure("TButton", padding=(0, 5, 0, 5), font='Verdana 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        self.columnconfigure(4, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)

        string_to_search_label = Label(self, text="Search a string: ")
        string_to_search_label.grid(row=0, column=0, rowspan=2)
        self.string_to_search_textfield = Entry(self)
        self.string_to_search_textfield.grid(row=0, column=1, rowspan=2, columnspan=2, sticky=W)
        self.string_to_search_textfield.bind('<Return>', self.get_string_from_textfield)
        self.compression_ratio_text = StringVar()
        self.compression_ratio_text.set('Compression Ratio: ')
        compression_ratio_label = Label(self, textvariable=self.compression_ratio_text).grid(row=0, column=2,
                                                                                             columnspan=4)

        Separator(self, orient=HORIZONTAL).grid(row=1)
        string_to_encode_label = Label(self, text="Encode a string: ")
        string_to_encode_label.grid(row=2, column=0, rowspan=2)
        self.string_to_encode_textfield = Entry(self)
        self.string_to_encode_textfield.grid(row=2, column=1, rowspan=2, columnspan=2, sticky=W)
        self.string_to_encode_textfield.bind('<Return>', self.get_string_from_textfield_to_encode)

        Separator(self, orient=HORIZONTAL).grid(row=3)
        self.area = Text(self)
        self.area.grid(row=4, column=0, columnspan=3, rowspan=1, padx=5, sticky=E + W)
        self.area.config(width=10, height=15)
        self.possible_options_text = StringVar()
        self.possible_options_text.set("Possible Options: ")
        self.possible_options_label = Label(self, textvariable=self.possible_options_text).grid(row=4, column=3,
                                                                                                sticky=N)

        huffman_coding_button = Button(self, text="Huffman",
                                       command=self.huffman_coding_callback).grid(row=5, column=0)
        arithmetic_coding_button = Button(self, text="Arithmetic Coding",
                                          command=self.arithmetic_coding_callback).grid(row=5, column=1)
        dictionary_coding_button = Button(self, text="Dictionary",
                                          command=self.dictionary_coding_callback).grid(row=5, column=2)
        elias_coding_button = Button(self, text="Elias",
                                     command=self.elias_coding_callback).grid(row=5, column=3)
        our_coding_button = Button(self, text="Elemental Coding",
                                   command=self.elemental_coding_callback).grid(row=5, column=4)
        self.pack()
        self.elemental_coding_callback()

    def get_string_from_textfield_to_encode(self, event):
        text_to_encode = self.string_to_encode_textfield.get()
        if text_to_encode == '':
            text_to_encode = 'a'
        if self.current_encoding == 1:
            self.huffman_coding.encode(text_to_encode)
            self.set_text_in_text_area(output)
            compression_ratio = self.huffman_coding.compression_ratio
            self.compression_ratio_text.set('Compression Ratio: ' + str(compression_ratio))
        if self.current_encoding == 2:
            pass
        if self.current_encoding == 3:
            pass
        if self.current_encoding == 4:
            pass
        if self.current_encoding == 5:
            self.elemental_coding.getElementList()
            self.elemental_coding.codeElemental(text_to_encode)
            self.elemental_coding.encodeText()
            output = self.elemental_coding.printCodedText()
            compression_ratio = self.elemental_coding.get_compression_ratio()
            self.compression_ratio_text.set('Compression Ratio: ' + str(compression_ratio))
            #self.set_text_in_text_area(output)

    def get_string_from_textfield(self, event):
        text_to_encode = self.string_to_sitemearch_textfield.get()
        possible_options = self.elemental_coding.lookForString(text_to_encode)
        self.possible_options_text.set('Possible Options: ' + possible_options)
        self.string_to_search_textfield.delete(END)

    def huffman_coding_callback(self):
        self.current_encoding = 1
        output = self.huffman_coding.encode_default_file()
        self.set_text_in_text_area(output)
        compression_ratio = self.huffman_coding.compression_ratio
        self.compression_ratio_text.set('Compression Ratio: ' + str(compression_ratio))
        print "HUFMAAN!"

    def arithmetic_coding_callback(self):
        self.current_encoding = 2
        text_to_encode = self.string_to_encode_textfield.get()
        if text_to_encode == '':
            text_to_encode = ' '
        for char in text_to_encode:
            if char not in arithmetic_intervals:
                can_encode = False
            else:
                can_encode = True
        if can_encode:
            codificacion = interval_coding(text_to_encode, arithmetic_intervals)
            self.compression_ratio_text.set(str(codificacion[2]))
        else:
            self.compression_ratio_text.set("Error: no en intervalos\n"
                                            "Si desea comprobar este metodo,"
                                            "introduce un string en el cuadro\n"
                                            "\"Encode text\"")

        print "Arithmetic!"

    def dictionary_coding_callback(self):
        self.current_encoding = 3
        contents = get_file_contents(os.getcwd() + '/pagina.txt')
        compress_text = self.dictionary_coding.compress(contents)
        compression_ratio = len(compress_text) / float(len(contents))
        self.compression_ratio_text.set('Compression Ratio: ' + str(compression_ratio) )
        compress_text = [str(item) for item in compress_text]
        self.set_text_in_text_area(''.join(compress_text))
        print "Dictionary!"

    def elias_coding_callback(self):
        self.current_encoding = 4
        text_to_encode = self.string_to_encode_textfield.get()
        if text_to_encode == '':
            text_to_encode = ' '
        for char in text_to_encode:
            if char not in elias_intervals:
                can_encode = False
            else:
                can_encode = True
        if can_encode:
            codificacion = interval_coding(text_to_encode, elias_intervals)
            self.compression_ratio_text.set(str(codificacion[2]) + "%")
        else:
            self.compression_ratio_text.set("Error: no en intervalos\n"
                                            "Si desea comprobar este metodo,"
                                            "introduce un string en el cuadro\n"
                                            "\"Encode text\"")


    def set_text_in_text_area(self, output):
        self.area.config(state=NORMAL)
        self.area.delete("1.0", END)
        self.area.insert(INSERT, output)
        self.area.config(state=DISABLED)

    def elemental_coding_callback(self):
        self.current_encoding = 5
        self.elemental_coding.getElementList()
        self.elemental_coding.processFile('pagina.txt')
        self.elemental_coding.encodeText()
        output = self.elemental_coding.printCodedText()
        self.set_text_in_text_area(output)
        compression_ratio = self.elemental_coding.get_compression_ratio()
        self.compression_ratio_text.set('Compression Ratio: ' + str(compression_ratio))
        print "Our Coding!"


def main():
    root = Tk()
    app = ElementalCodingGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
