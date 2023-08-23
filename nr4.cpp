#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <functional>
#include <unordered_map>

typedef std::pair<int, int> Segment;
typedef std::pair<double, double> Point;

Segment make_segment(int first, int second) {
    return std::make_pair(first, second);
}

Point make_point(double first, double second) {
    return std::make_pair(first, second);
}

std::vector<Segment> generate_all_connections(int n) {
    std::vector<Segment> connections;
    for (int i = 0; i < 2 * n; ++i) {
        for (int j = i + 1; j < 2 * n; ++j) {
            connections.push_back(make_segment(i, j));
        }
    }
    return connections;
}

std::vector<Segment> explore_path(
    Segment node,
    std::vector<int> banned,
    std::vector<Segment> path,
    int n,
    const std::unordered_map<int, std::vector<Segment>>& jumps_made
) {
    int m = node.first;
    int index = node.second;

    if (m < 0) {
        return {};
    }

    std::vector<Segment> filtered_array;
    if (m == n - 1) {
        filtered_array.push_back(jumps_made.at(m)[0]);
    } else {
        for (const Segment& segment : jumps_made.at(m)) {
            if (std::all_of(banned.begin(), banned.end(), [&](int num) {
                    return num != segment.first && num != segment.second;
                })) {
                filtered_array.push_back(segment);
            }
        }
    }

    for (size_t i = 0; i < filtered_array.size(); ++i) {
        const Segment& segment = filtered_array[i];
        Segment next_node = make_segment(m - 1, i);
        std::vector<int> next_banned = banned;
        next_banned.push_back(segment.first);
        next_banned.push_back(segment.second);
        std::vector<Segment> new_path = path;
        new_path.push_back(segment);

        if (new_path.size() == static_cast<size_t>(n)) {
            return new_path;
        }

        std::vector<Segment> solution_path = explore_path(next_node, next_banned, new_path, n, jumps_made);
        if (!solution_path.empty()) {
            return solution_path;
        }
    }

    return {};
}

std::vector<Segment> generate_solutions(const std::vector<Segment>& connections, int n, const std::vector<Point>& corners) {
    std::unordered_map<int, std::vector<Segment>> jumps_made;

    for (const Segment& segment : connections) {
        int index;
        if (segment.second == (2 * n) - 1 && segment.first == 0) {
            index = 0;
        } else {
            int diff = std::abs(segment.second - segment.first - 1);
            index = (diff <= (n - 1)) ? diff : (diff - 2 * (diff - (n - 1)));
        }
        jumps_made[index].push_back(segment);
    }

    std::vector<Segment> solutions;
    Segment root = make_segment(n - 1, 0);
    solutions = explore_path(root, {}, {}, n, jumps_made);
    return solutions;
}

int main() {
    int start_n, end_n;
    std::cout << "Startwert für n (>= 2) eingeben: ";
    std::cin >> start_n;
    std::cout << "Endwert für n (>= Startwert) eingeben: ";
    std::cin >> end_n;

    if (start_n < 2 || end_n < start_n) {
        std::cout << "Ungültige Eingabe. Startwert muss >= 2 sein und Endwert muss >= Startwert sein." << std::endl;
        return 1;
    }

    for (int n = start_n; n <= end_n; ++n) {
        std::vector<Point> corners;
        for (int i = 0; i < 2 * n; ++i) {
            double angle = static_cast<double>(i) * std::acos(-1) / static_cast<double>(n);
            corners.push_back(make_point(std::cos(angle), std::sin(angle)));
        }

        std::vector<Segment> all_connections = generate_all_connections(n);
        std::vector<Segment> gsl = generate_solutions(all_connections, n, corners);

        std::cout << "Für n = " << n << ": ";
        if (gsl.empty()) {
            std::cout << "Keine Lösung." << std::endl;
        } else {
            std::cout << "Eine Lösung." << std::endl;
        }
    }

    return 0;
}
