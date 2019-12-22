class Node 
    attr_accessor :data, :next_node, :previous_node

    def initialize(data)
     @data = data   
    end
end

class DoublyLinkedList 
    attr_accessor :first_node, :last_node
    def initialize(first_node=nil, last_node=nil)
        @first_node =first_node
        @last_node =last_node
    end

    def insert_at_end(value)
      new_node = Node.new(value)
    
      # if there are no elements yet in the linked list
      if !first_node
        puts "missing first node"
        @first_node = new_node
        @last_node = new_node
      else
        puts 'first node found'
        new_node.previous_node = @last_node
        @last_node.next_node = new_node
        @last_node = new_node
        puts @last_node.data
      end
    end
end

double_linked_list = DoublyLinkedList.new()
puts 'before'
puts double_linked_list
puts 'after'
double_linked_list.insert_at_end(1)
puts double_linked_list
double_linked_list.insert_at_end(2)
puts double_linked_list

puts 'start node'
double_linked_list.first_node.data

puts 'end node'
double_linked_list.last_node.data
