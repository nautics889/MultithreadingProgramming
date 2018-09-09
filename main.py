import sys, getopt, ast
from graphviz import Digraph
from functools import reduce

class Graph_Model(Digraph):
    def __init__(self, graph_dictionary, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(graph_dictionary)
        self.__graph_dictionary = graph_dictionary
        self.build_graph()
        self.find_eccentricity()
        #self.view()

    def build_graph(self):
        for vertex in self.__graph_dictionary.keys():
            self.node(str(vertex), str(vertex))
            print(self.__graph_dictionary[vertex])
            for toward, weight in self.__graph_dictionary[vertex]:
                self.edge(str(vertex), str(toward), label=str(weight))

    #def find_center(self):
        #for vertex in self.__graph_dictionary.keys():

    def find_eccentricity(self):
        print('PATHS: \n', self.find_all_paths(self.__graph_dictionary['bar'], self.__graph_dictionary['foobar']))

    def find_all_paths(self, start_v, end_v, path=[]):
        path.append(start_v)
        if start_v == end_v:
            return path
        paths = []
        for vertex in self.__graph_dictionary.keys():
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_v, path)
                for p in extended_paths:
                    paths.append(p)
        return paths

class Program_Interface:
    def __init__(self, args):
        self.__filename = self.get_args(args)
        with open('%s' % self.__filename) as f:
            self.__graph_dictionary = ast.literal_eval(f.read())
        self.custom_graph = Graph_Model(self.__graph_dictionary, comment='Common Graph', filename='custom_graph.gv')

    def get_args(self, args):
        try:
            opts, args = getopt.getopt(args, 'hf:', ['file=',])
        except getopt.GetoptError:
            print('Argument error. Did you forget to specify filename with a graph?')
            sys.exit(1)
        for opt, arg in opts:
            if '-h' in opt:
                pass
            elif opt in ('-f', '--file'):
                return str(arg)

if __name__ == '__main__':
    prog = Program_Interface(sys.argv[1:])